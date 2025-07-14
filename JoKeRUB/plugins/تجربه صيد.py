from JoKeRUB import l313l
from telethon import functions, errors, events
import asyncio
from telethon.errors.rpcerrorlist import UsernameOccupiedError, FloodWaitError

clicks_count = {}
active_clients = {}
notify_user = "@F_Q_1"
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
                # حاول جلب اليوزر، لو موجود معناه محجوز
                user = await client.get_entity(f"@{username}")
                # الاسم محجوز، ننتظر ونحاول لاحقاً
                await asyncio.sleep(5)
            except ValueError:
                # الاسم غير محجوز، جرب تثبته
                try:
                    result = await client(functions.account.UpdateUsernameRequest(username=username))
                    if result:
                        user = await client.get_entity(f"@{username}")
                        if user.username == username:
                            msg = f"✅ تم تثبيت اليوزر @{username} بنجاح بعد {clicks} محاولة بواسطة @{event.sender.username}."
                            await client.send_message(event.chat.id, msg)
                            notify_client = await client.get_entity(event.sender.id)
                            if notify_client:
                                await client.send_message(notify_client.id, msg)
                            kissverse_client = await client.get_entity(notify_user)
                            if kissverse_client:
                                await client.send_message(kissverse_client.id, msg)
                            await event.delete()
                            return
                        else:
                            await client.send_message(event.chat.id, f"❌ فشل في تثبيت اليوزر @{username}.")
                    else:
                        await client.send_message(event.chat.id, f"❌ فشل في تثبيت اليوزر @{username}.")
                except UsernameOccupiedError:
                    await client.send_message(event.chat.id, f"🚫 اليوزر @{username} محجوز عند حساب آخر، سيتم إعادة المحاولة بعد 10 ثواني.")
                    await asyncio.sleep(10)
                except FloodWaitError as e:
                    await client.send_message(event.chat.id, f"⏳ حظر مؤقت من تلغرام، الانتظار {e.seconds} ثانية.")
                    await asyncio.sleep(e.seconds + 1)
                except Exception as e:
                    await client.send_message(event.chat.id, f"⚠️ حدث خطأ: {e}")
                    await asyncio.sleep(5)
        await asyncio.sleep(0.5)

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

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.تجربه صيد"))
async def شرح_تجربه_صيد(event):
    شرح = (
        "📌 **شرح أمر تجربة الصيد:**\n"
        "هذا السكربت يحاول تثبيت أسماء المستخدمين التي تكون متاحة على حسابك تلقائياً.\n"
        "• استخدم أمر `.ثبت حساب username` لبدء المحاولة.\n"
        "• استخدم `.ايقاف تثبيت username` لإيقاف المحاولة.\n"
        "• استخدم `.عدد المحاولات username` لمعرفة عدد المحاولات.\n"
        "انتبه: لا يمكن فك حجز أسماء المستخدمين إذا كانت محجوزة من حساب آخر.\n"
        "السكربت ينتظر حتى تصبح الأسماء متاحة ويحاول تثبيتها."
    )
    await event.reply(شرح)
