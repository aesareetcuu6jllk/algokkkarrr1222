import re
from telethon import events
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/+DGe8lA2FvsM4ZTRi"
pending_checks = {}
activated_users = set()  # لتخزين الذين فعّلوا الفحص

@l313l.on(events.NewMessage(pattern=r"^\.تفعيل\s+فحص\s+اليوزرات$", incoming=True))
async def activate(event):
    user_id = event.sender_id
    if user_id in activated_users:
        await event.respond("✅ أنت مفعل سابقًا.")
        return

    activated_users.add(user_id)
    await event.respond(
        f"✅ تم تفعيل فحص اليوزرات لك.\n"
        f"🔗 الرجاء الانضمام إلى المجموعة:\n{CHECK_GROUP_LINK}\n"
        "ثم استخدم الأمر:\n`.يوزر @username` أو قم بالرد على رسالة تحتوي المعرف وأرسل `.يوزر`"
    )

@l313l.on(events.NewMessage(pattern=r"^.يوزر(?:\s+(.*))?", incoming=True))
async def sandal_cmd(event):
    user_id = event.sender_id
    if user_id not in activated_users:
        await event.respond("❌ لازم تفعيل فحص اليوزرات بالأمر:\n`.تفعيل فحص اليوزرات`")
        return

    me = await l313l.get_me()
    if user_id != me.id:
        return  # الأمر يعمل فقط من صاحب الحساب (اختياري، لو تريد تزيل هذا الشرط احذفه)

    input_text = event.pattern_match.group(1)
    if not input_text:
        reply = await event.get_reply_message()
        if reply:
            input_text = reply.text or ""
        else:
            return await event.reply("❌ يرجى كتابة المعرف أو الرد على رسالة.")

    usernames = re.findall(r"@[\w\d_]{5,32}", input_text)
    if not usernames:
        return await event.reply("❌ لم يتم العثور على أي يوزر بالرسالة.")

    # تأكد أن الحساب مشترك يدويًا في المجموعة، بدون انضمام تلقائي هنا
    for user in usernames:
        try:
            sent_msg = await l313l.send_message(CHECK_GROUP_LINK, f"فحص {user}")
            pending_checks[sent_msg.id] = (event, user)
            await event.reply(f"⏳ جاري الفحص للمعرف: {user}")
        except Exception as e:
            await event.reply(f"❌ فشل إرسال الفحص لليوزر {user}:\n{e}")

@l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK))
async def on_group_reply(event):
    if event.is_reply:
        replied_msg_id = event.reply_to_msg_id
        if replied_msg_id in pending_checks:
            user_event, username = pending_checks.pop(replied_msg_id)
            await user_event.reply(f"📩 نتيجة فحص {username}:\n{event.text}")
