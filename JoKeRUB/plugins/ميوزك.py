from telethon import events
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/sekknft"

@l313l.on(events.NewMessage(pattern=r"^\.يوت\s+(.*)"))
async def forward_to_group(event):
    input_text = event.pattern_match.group(1)

    # إرسال الرسالة للقروب
    sent_msg = await l313l.send_message(CHECK_GROUP_LINK, f"يوت {input_text}")

    # متابعة أي رد على هذه الرسالة فقط
    @l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK, reply_to=sent_msg.id))
    async def reply_handler(reply_event):
        if reply_event.audio:
            # يرسل البصمة **لك فقط**، الحساب الذي كتب الأمر
            await l313l.send_file(event.sender_id, reply_event.audio)
        else:
            await l313l.send_message(event.sender_id, f"❌ لم يتم العثور على ملف صوتي لـ: {input_text}")

        # بعد الإرسال، نحذف الهاندلر
        l313l.remove_event_handler(reply_handler)
