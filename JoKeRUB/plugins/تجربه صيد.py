from JoKeRUB import l313l
from telethon import functions, errors, events
import asyncio

clicks_count = {}
active_clients = {}
semaphore = asyncio.Semaphore(1)

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.ثبت حساب\s+(\S+)"))
async def تثبيت_اليوزر(event):
    username = event.pattern_match.group(1)
    if username.startswith("@"):
        username = username[1:]
    client = event.client

    await event.reply(f"⏳ جاري محاولة تثبيت اليوزر @{username} على الحساب...")

    active_clients[client] = username
    clicks = 0

    while True:
        if active_clients.get(client) != username:
            await client.send_message(event.chat.id, f"🛑 تم إيقاف التثبيت لليوزر @{username}.")
            return
        async with semaphore:
            clicks += 1
            clicks_count[username] = clicks
            try:
                # تحقق إذا اليوزر محجوز
                user = await client.get_entity(f"@{username}")
                await asyncio.sleep(5)
            except ValueError:
                try:
                    result = await client(functions.account.UpdateUsernameRequest(username=username))
                    if result:
                        user = await client.get_entity(f"@{username}")
                        if user.username == username:
                            await client.send_message(event.chat.id, f"✅ تم تثبيت اليوزر @{username} على الحساب بنجاح بعد {clicks} محاولة.")
                            await event.delete()
                            return
                        else:
                            await client.send_message(event.chat.id, f"❌ فشل في تثبيت اليوزر @{username}.")
                    else:
                        await client.send_message(event.chat.id, f"❌ فشل في تثبيت اليوزر @{username}.")
                except errors.UsernameOccupiedError:
                    await client.send_message(event.chat.id, f"🚫 اليوزر @{username} محجوز عند حساب آخر، إعادة المحاولة بعد 10 ثواني.")
                    await asyncio.sleep(10)
                except errors.FloodWaitError as e:
                    await client.send_message(event.chat.id, f"⏳ حظر مؤقت من تلغرام، الانتظار {e.seconds} ثانية.")
                    await asyncio.sleep(e.seconds + 1)
                except Exception as e:
                    await client.send_message(event.chat.id, f"⚠️ حدث خطأ: {e}")
                    await asyncio.sleep(5)
        await asyncio.sleep(0.5)

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.ثبت قناه\s+(\S+)"))
async def تثبيت_يوزر_على_القناه(event):
    username = event.pattern_match.group(1)
    if username.startswith("@"):
        username = username[1:]
    client = event.client

    try:
        channel_entity = await client.get_entity(event.chat_id)

        await event.reply(f"⏳ جاري محاولة تثبيت اليوزر @{username} على القناة/الجروب الحالي...")

        active_clients[client] = username
        clicks = 0

        while True:
            if active_clients.get(client) != username:
                await client.send_message(event.chat.id, f"🛑 تم إيقاف تثبيت اليوزر @{username} على القناة.")
                return
            async with semaphore:
                clicks += 1
                clicks_count[username] = clicks
                try:
                    result = await client(functions.channels.UpdateUsernameRequest(
                        channel=channel_entity,
                        username=username
                    ))

                    updated_channel = await client.get_entity(event.chat_id)
                    if updated_channel.username == username:
                        await client.send_message(event.chat.id, f"✅ تم تثبيت اليوزر @{username} على القناة/الجروب بنجاح بعد {clicks} محاولة.")
                        await event.delete()
                        return
                    else:
                        await client.send_message(event.chat.id, f"❌ فشل في تثبيت اليوزر @{username} على القناة/الجروب.")

                except errors.UsernameOccupiedError:
                    await client.send_message(event.chat.id, f"🚫 اليوزر @{username} محجوز عند حساب/قناة آخر، إعادة المحاولة بعد 10 ثواني.")
                    await asyncio.sleep(10)
                except errors.FloodWaitError as e:
                    await client.send_message(event.chat.id, f"⏳ حظر مؤقت من تلغرام، الانتظار {e.seconds} ثانية.")
                    await asyncio.sleep(e.seconds + 1)
                except Exception as e:
                    await client.send_message(event.chat.id, f"⚠️ حدث خطأ: {e}")
                    await asyncio.sleep(5)
            await asyncio.sleep(0.5)

    except Exception as e:
        await event.reply(f"⚠️ حدث خطأ أثناء جلب القناة: {e}")

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.عدد المحاولات\s+(\S+)"))
async def عرض_عدد_الضغطات(event):
    username = event.pattern_match.group(1)
    if username.startswith("@"):
        username = username[1:]
    if username in clicks_count:
        await event.reply(f"📊 عدد المحاولات لليوزر @{username}: {clicks_count[username]}")
    else:
        await event.reply(f"❌ لم يتم بدء تثبيت اليوزر @{username} بعد.")

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف تثبيت\s+(\S+)"))
async def ايقاف_التثبيت(event):
    username = event.pattern_match.group(1)
    if username.startswith("@"):
        username = username[1:]
    for client, active_username in list(active_clients.items()):
        if active_username == username:
            del active_clients[client]
            await event.reply(f"🛑 تم إيقاف التثبيت لليوزر @{username}.")
            return
    await event.reply(f"❌ لا يوجد تثبيت جاري لليوزر @{username}.")

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر اليوزرات"))
async def شرح_تجربه_صيد(event):
    شرح = (
        "📌 **شرح اوامر نقل اليوزرات :**\n"
        "هذا السكربت يحاول تثبيت أسماء المستخدمين التي تكون متاحة على حسابك أو قناتك تلقائياً.\n"
        "• استخدم أمر `.ثبت حساب username` لبدء تثبيت على الحساب.\n"
        "• استخدم أمر `.ثبت قناه username` لبدء تثبيت على القناة/الجروب الذي أنت مشرف فيه.\n"
        "• استخدم `.ايقاف تثبيت username` لإيقاف المحاولة.\n"
        "• استخدم `.عدد المحاولات username` لمعرفة عدد المحاولات.\n"
        "انتبه: لا يمكن فك حجز أسماء المستخدمين إذا كانت محجوزة من حساب أو قناة آخر.\n"
        "السكربت ينتظر حتى تصبح الأسماء متاحة ويحاول تثبيتها."
    )
    await event.reply(شرح)

