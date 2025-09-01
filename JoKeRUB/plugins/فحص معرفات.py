import re
from telethon import events, Button
from JoKeRUB import l313l

# رابط الكروب للفحص
CHECK_GROUP_LINK = "https://t.me/sekknft"

# لتخزين الرسائل المعلقة
pending_checks = {}
# لتخزين نتائج المعرفات
usernames_map = {}

@l313l.on(events.NewMessage(pattern=r"^.معرفاته(?:\s+(.*))?"))
async def sandal_cmd(event):
    me = await l313l.get_me()
    if event.sender_id != me.id:
        return  # فقط صاحب الحساب يستخدم الأمر

    input_text = event.pattern_match.group(1)
    if not input_text:
        reply = await event.get_reply_message()
        if reply:
            input_text = reply.text or ""
        else:
            return await event.reply("❌ يرجى كتابة المعرف أو الرد على رسالة.")

    usernames = re.findall(r"@[\w\d_]{5,32}", input_text)
    if not usernames:
        return await event.reply("❌ لم يتم العثور على أي معرف بالرسالة.")

    for user in usernames:
        try:
            sent_msg = await l313l.send_message(CHECK_GROUP_LINK, f"فحص {user}")
            pending_checks[sent_msg.id] = (event, user)
        except Exception as e:
            await event.reply(f"❌ فشل إرسال الفحص للمعرف {user}:\n{e}")


@l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK))
async def on_group_reply(event):
    if event.is_reply:
        replied_msg_id = event.reply_to_msg_id
        if replied_msg_id in pending_checks:
            user_event, username = pending_checks.pop(replied_msg_id)

            # اول شي يبعثلك انه جاري الجلب
            msg = await user_event.reply("⏳ يتم جلب المعرفات ...")

            text = event.text
            # استخراج المعرفات إذا موجودة
            found_users = re.findall(r"@[\w\d_]{3,32}", text)
            if found_users:
                usernames_map[username] = found_users
                await msg.edit(
                    f"{text}",
                    buttons=[Button.inline("عرض كل المعرفات", data=f"show:{username}")]
                )
            else:
                await msg.edit(f"{text}")


@l313l.on(events.CallbackQuery(pattern=b"show:(.+)"))
async def show_usernames(event):
    username = event.pattern_match.group(1).decode("utf-8")
    users = usernames_map.get(username, [])
    if not users:
        return await event.answer("❌ لا توجد معرفات إضافية.", alert=True)

    msg = f"📂 المعرفات المرتبطة بـ {username}:\n" + "\n".join(users)
    await event.edit(msg)

