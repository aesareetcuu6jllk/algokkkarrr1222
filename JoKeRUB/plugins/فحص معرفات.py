import re
from telethon import events
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/+DGe8lA2FvsM4ZTRi"
pending_checks = {}
checking_enabled = False  # تفعيل الفحص

# أمر التفعيل
@l313l.on(events.NewMessage(pattern=r"^\.تفعيل فحص اليوزرات$"))
async def enable_check(event):
    global checking_enabled
    me = await l313l.get_me()
    if event.sender_id != me.id:
        return  # فقط صاحب الحساب
    checking_enabled = True
    await event.reply(
        f"✅ تم تفعيل فحص اليوزرات.\n"
        f"📌 يرجى أولاً الانضمام للقروب من هنا:\n{CHECK_GROUP_LINK}\n"
        f"ثم استعمل الأمر:\n`.يوزر @المعرف` أو بالرد على رسالة."
    )

# أمر الفحص
@l313l.on(events.NewMessage(pattern=r"^.يوزر(?:\s+(.*))?"))
async def sandal_cmd(event):
    global checking_enabled
    me = await l313l.get_me()
    if event.sender_id != me.id:
        return

    if not checking_enabled:
        return await event.reply("❌ يجب أولاً كتابة `.تفعيل فحص اليوزرات`.")

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

    for user in usernames:
        try:
            sent_msg = await l313l.send_message(CHECK_GROUP_LINK, f"فحص {user}")
            pending_checks[sent_msg.id] = (event, user)
        except Exception as e:
            await event.reply(f"❌ فشل إرسال الفحص لليوزر {user}:\n{e}")

# استقبال الرد من القروب
@l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK))
async def on_group_reply(event):
    if event.is_reply:
        replied_msg_id = event.reply_to_msg_id
        if replied_msg_id in pending_checks:
            user_event, username = pending_checks.pop(replied_msg_id)
            await user_event.reply(f"{event.text}")

