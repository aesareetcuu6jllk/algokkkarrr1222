from telethon import events
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/sekknft"

# نجيب الايدي الخاص بالحساب مال الجلسة
async def get_owner_id():
    me = await l313l.get_me()
    return me.id

@l313l.on(events.NewMessage(pattern=r"^\.يوت\s+(.*)"))
async def forward_to_group(event):
    owner_id = await get_owner_id()

    # اذا مو صاحب الحساب => تجاهل
    if event.sender_id != owner_id:
        return

    input_text = event.pattern_match.group(1)

    # نرسل الرسالة للقروب
    sent_msg = await l313l.send_message(CHECK_GROUP_LINK, f"يوت {input_text}")

    replies = {"count": 0}

    @l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK, reply_to=sent_msg.id))
    async def reply_handler(reply_event):
        replies["count"] += 1

        if replies["count"] == 1:
            # أول رد نتجاهله
            return
        elif replies["count"] == 2:
            # الرد الثاني فقط
            if reply_event.audio:
                await l313l.send_file(event.chat_id, reply_event.audio, reply_to=event.id)
            else:
                await l313l.send_message(event.chat_id, f"❌ ماكو بصمة لـ: {input_text}", reply_to=event.id)

            l313l.remove_event_handler(reply_handler)
