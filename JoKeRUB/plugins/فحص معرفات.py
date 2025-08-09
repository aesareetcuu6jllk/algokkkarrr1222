from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/+DGe8lA2FvsM4ZTRi"

pending_checks = {}

@l313l.on(events.NewMessage(pattern=r"^.يوزر(?:\s+(.*))?"))
async def sandal_cmd(event: events.NewMessage.Event):
    input_text = event.pattern_match.group(1)

    if not input_text:
        reply = await event.get_reply_message()
        if reply and reply.sender:
            username = reply.sender.username
            if not username:
                return await event.reply("❌ المستخدم لا يملك يوزر.")
            input_text = f"@{username}"
        else:
            return await event.reply("❌ يرجى كتابة المعرف أو الرد على رسالة.")

    # الانضمام للقروب تلقائي
    try:
        if CHECK_GROUP_LINK.startswith("https://t.me/+"):
            hash_part = CHECK_GROUP_LINK.split("+")[1]
            await l313l(ImportChatInviteRequest(hash_part))
        elif CHECK_GROUP_LINK.startswith("https://t.me/"):
            username = CHECK_GROUP_LINK.split("https://t.me/")[1]
            await l313l(JoinChannelRequest(username))
    except Exception:
        pass

    try:
        sent_msg = await l313l.send_message(CHECK_GROUP_LINK, f"فحص {input_text}")
    except Exception as e:
        return await event.reply(f"❌ فشل إرسال الفحص داخل المجموعة:\n{e}")

    pending_checks[sent_msg.id] = event

@l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK))
async def on_group_reply(event: events.NewMessage.Event):
    if event.is_reply:
        replied_msg_id = event.reply_to_msg_id
        if replied_msg_id in pending_checks:
            user_event = pending_checks.pop(replied_msg_id)
            await user_event.reply(f"{event.text}")
