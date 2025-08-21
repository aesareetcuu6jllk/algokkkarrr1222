from telethon import events
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/sekknft"

# لتخزين الرسائل الأخيرة التي أرسلتها أنت مؤقتًا
last_sent_msg = None
waiting_for_second = False

@l313l.on(events.NewMessage(pattern=r"^\.يوت\s+(.*)"))
async def forward_to_group(event):
    global last_sent_msg, waiting_for_second
    input_text = event.pattern_match.group(1)

    # إرسال الرسالة للقروب
    last_sent_msg = await l313l.send_message(CHECK_GROUP_LINK, f"يوت {input_text}")
    waiting_for_second = True  # ننتظر الرد الثاني فقط

@l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK))
async def check_group_reply(event):
    global last_sent_msg, waiting_for_second
    if last_sent_msg is None:
        return

    # نتأكد أن هذه الرسالة رد على الرسالة التي أرسلها البوت
    if event.is_reply and event.reply_to_msg_id == last_sent_msg.id:
        if waiting_for_second:
            # أول رد يتم تجاهله
            waiting_for_second = False
            return
        else:
            # الرد الثاني
            if event.audio:
                await l313l.send_file(last_sent_msg.sender_id, event.audio)
            else:
                await l313l.send_message(last_sent_msg.sender_id, "❌ لم يتم العثور على ملف صوتي.")
            # بعد الإرسال، نعيد تعيين المتغيرات
            last_sent_msg = None
            waiting_for_second = False
