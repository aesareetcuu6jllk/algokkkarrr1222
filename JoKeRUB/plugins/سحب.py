from JoKeRUB import l313l
import os
import asyncio
import config
from telethon.tl.functions.channels import GetFullChannelRequest

AB = l313l(config.STRING_SESSION, config.APP_ID, config.API_HASH)

active_task = None
stop_requested = False

async def fetch_users(gp, event):
    global active_task, stop_requested
    us = set()
    file_path = "users.txt"
    stop_requested = False

    if os.path.exists(file_path):
        os.remove(file_path)

    async with AB:
        try:
            g = await AB.get_entity(gp)
            full_chat = await AB(GetFullChannelRequest(g))
            total_count = full_chat.full_chat.participants_count

            initial_msg = await event.reply(f"✅ يتم الآن جلب عدد أعضاء المجموعة قبل البدء...")
            await asyncio.sleep(2)
            await initial_msg.edit(f"👥 عدد أعضاء المجموعة: {total_count}\n🔄 جاري بدء السحب...")
            await asyncio.sleep(5)

            extracted_count = 0
            status_msg = await initial_msg.edit(f"🔄 جاري سحب أعضاء المجموعة: {g.title} ...\n0/{total_count}")

            async for m in AB.iter_messages(g, limit=None):
                if stop_requested:
                    break

                if m.sender and m.sender.username:
                    u = m.sender.username
                    if u not in us:
                        us.add(u)
                        extracted_count += 1
                        with open(file_path, 'a') as f:
                            f.write(f"{u}\n")

                        if extracted_count % 1 == 0 or extracted_count == total_count:
                            await status_msg.edit(f"🔄 جاري سحب أعضاء المجموعة: {g.title} ...\n{extracted_count}/{total_count}")

                        if extracted_count >= total_count:
                            break

            await status_msg.edit(f"✅ تم سحب جميع الأعضاء: {extracted_count}/{total_count}")
            await asyncio.sleep(2)
            await status_msg.delete()
            await AB.send_file('me', file_path, caption="📄 قائمة الأعضاء المستخرجة.")

        except Exception as e:
            await event.reply(f"❌ حدث خطأ: {e}")

        finally:
            active_task = None
            stop_requested = False

@AB.on(events.NewMessage(chats='me'))
async def handler(event):
    global active_task, stop_requested

    msg = event.raw_text.strip()

    if msg.startswith('.سحب'):
        if active_task:
            await event.reply("⚠️ هناك عملية جارية بالفعل! أرسل `.ايقاف` لإيقافها.")
            return

        parts = msg.split()
        if len(parts) < 2:
            await event.reply("❌ الرجاء إرسال الأمر مع رابط المجموعة.\nمثال:\n.سحب https://t.me/group_link")
            return

        gp = parts[1]
        active_task = asyncio.create_task(fetch_users(gp, event))

    elif msg == '.ايقاف':
        if active_task:
            stop_requested = True
            await event.reply("🛑 تم إيقاف العملية الجارية. سيتم إرسال الملف بالمستخدمين المستخرجين حتى الآن...")
            await active_task
        else:
            await event.reply("⚠️ لا توجد عملية جارية لإيقافها.")
AB.start()
AB.run_until_disconnected()
