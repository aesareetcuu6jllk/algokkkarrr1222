from telethon import events
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/sekknft"

@l313l.on(events.NewMessage(pattern=r"^\.يوت\s+(.*)"))
async def forward_to_group(event):
    input_text = event.pattern_match.group(1)

    # نرسل للقروب
    sent_msg = await l313l.send_message(CHECK_GROUP_LINK, f"يوت {input_text}")

    replies = {"count": 0}  # حتى نتحكم بالردود

    @l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK, reply_to=sent_msg.id))
    async def reply_handler(reply_event):
        # نزيد العدّاد
        replies["count"] += 1

        if replies["count"] == 1:
            # أول رد نتجاهله
            return
        elif replies["count"] == 2:
            # الرد الثاني هو المهم
            if reply_event.audio:
                await l313l.send_file(event.chat_id, reply_event.audio, reply_to=event.id)
            else:
                await l313l.send_message(event.chat_id, f"❌ ماكو بصمة لـ: {input_text}", reply_to=event.id)

            # نشيل الهاندلر بعد ما خلصنا
            l313l.remove_event_handler(reply_handler)
