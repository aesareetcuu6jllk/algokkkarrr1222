import re
import asyncio
from telethon import events
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/sekknft"

pending_checks = {}
usernames_map = {}

@l313l.on(events.NewMessage(pattern=r"^.معرفاته(?:\s+(.*))?"))
async def sandal_cmd(event):
    me = await l313l.get_me()
    if event.sender_id != me.id:
        return

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
    # لازم يكون رد على رسالة فحص مالنا
    if not event.is_reply:
        return

    replied_msg_id = event.reply_to_msg_id
    if replied_msg_id not in pending_checks:
        return

    user_event, username = pending_checks.pop(replied_msg_id)

    # رسالة انتظار بمكان تنفيذ الأمر
    wait_msg = await user_event.reply("⏳ يتم جلب المعرفات ...")

    # نحاول نضغط زر "عرض كل اليوزرات" تلقائي
    final_text = event.text or ""
    try:
        # إذا موجود زر بنفس الرسالة
        if getattr(event, "buttons", None):
            # نضغط الزر بالنص (تقدر تغيّر النص إذا يختلف)
            await event.click(text="عرض كل اليوزرات")

            # ننتظر تعديل الرسالة أو رسالة جديدة من نفس البوت
            msg_id = event.id
            bot_id = event.sender_id

            edited = None
            try:
                edited = await l313l.wait_for(
                    events.MessageEdited(chats=CHECK_GROUP_LINK, ids=msg_id),
                    timeout=8
                )
            except asyncio.TimeoutError:
                edited = None

            if edited:
                final_text = edited.text or final_text
            else:
                try:
                    new_msg = await l313l.wait_for(
                        events.NewMessage(chats=CHECK_GROUP_LINK, from_users=bot_id),
                        timeout=5
                    )
                    final_text = new_msg.text or final_text
                except asyncio.TimeoutError:
                    pass
        # إذا ماكو أزرار، ناخذ النص كما هو
    except Exception:
        # أي خطأ بالضغط نرجع للنص الحالي
        pass

    # نستخرج المعرفات من النص النهائي
    found_users = re.findall(r"@[\w\d_]{3,32}", final_text)

    # نخزن للرجوع لاحقًا (اختياري)
    if found_users:
        usernames_map[username] = {
            "users": found_users,
            "chat_id": user_event.chat_id,
            "reply_to": user_event.id
        }

    # نرسل المحتوى إليك مباشرة، مع القائمة إذا موجودة
    out = final_text
    if found_users:
        out += "\n\n📂 المعرفات المرتبطة بـ {}:\n{}".format(
            username, "\n".join(found_users)
        )

    await l313l.send_message(user_event.chat_id, out, reply_to=user_event.id)
    await wait_msg.delete()

