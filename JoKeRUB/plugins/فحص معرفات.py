
import re
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/+DGe8lA2FvsM4ZTRi"

pending_checks = {}

@l313l.on(events.NewMessage(pattern=r"^.يوزر(?:\s+(.*))?"))
async def sandal_cmd(event: events.NewMessage.Event):
    input_text = event.pattern_match.group(1)

    # إذا ماكو نص، ناخذ من الرسالة اللي عامل عليها ريبلَاي
    if not input_text:
        reply = await event.get_reply_message()
        if reply:
            input_text = reply.text or ""
        else:
            return await event.reply("❌ يرجى كتابة المعرف أو الرد على رسالة.")

    # استخراج جميع اليوزرات بصيغة @username
    usernames = re.findall(r"@[\w\d_]{5,32}", input_text)
    if not usernames:
        return await event.reply("❌ لم يتم العثور على أي يوزر بالرسالة.")

    # الانضمام للقروب إذا مو منضم
    try:
        if CHECK_GROUP_LINK.startswith("https://t.me/+"):
            hash_part = CHECK_GROUP_LINK.split("+")[1]
            await l313l(ImportChatInviteRequest(hash_part))
        elif CHECK_GROUP_LINK.startswith("https://t.me/"):
            username = CHECK_GROUP_LINK.split("https://t.me/")[1]
            await l313l(JoinChannelRequest(username))
    except Exception:
        pass

    # فحص كل يوزر وإضافة للمتابعة
    for user in usernames:
        try:
            sent_msg = await l313l.send_message(CHECK_GROUP_LINK, f"فحص {user}")
            pending_checks[sent_msg.id] = (event, user)
        except Exception as e:
            await event.reply(f"❌ فشل إرسال الفحص لليوزر {user}:\n{e}")

@l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK))
async def on_group_reply(event: events.NewMessage.Event):
    if event.is_reply:
        replied_msg_id = event.reply_to_msg_id
        if replied_msg_id in pending_checks:
            user_event, username = pending_checks.pop(replied_msg_id)
            await user_event.reply(f"🔎 النتيجة لليوزر {username}:\n{event.text}")
