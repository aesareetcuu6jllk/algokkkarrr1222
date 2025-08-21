from telethon import events
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/sekknft"

# تخزين حالة كل مستخدم: 'waiting' = تم إرسال الأمر للقروب، 'ready' = جاهز لإرسال الملف
user_state = {}

@l313l.on(events.NewMessage(pattern=r"^\.يوت\s+(.*)"))
async def forward_to_group(event):
    input_text = event.pattern_match.group(1)
    user_id = event.sender_id

    # إعادة صياغة الأمر لإرساله للقروب
    message_to_group = f"يوت {input_text}"
    sent_msg = await l313l.send_message(CHECK_GROUP_LINK, message_to_group)

    # حفظ حالة المستخدم والرسالة التي أرسلها البوت بالقروب
    user_state[user_id] = {
        'status': 'waiting',  # أول رد سيتم تجاهله
        'input_text': input_text,
        'group_msg_id': sent_msg.id
    }

# متابعة أي رسالة جديدة بالقروب
@l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK))
async def check_group_reply(event):
    for user_id, info in list(user_state.items()):
        # نتحقق أن هذه الرسالة هي الرد على رسالة البوت بالقروب
        if event.is_reply and event.reply_to_msg_id == info['group_msg_id']:
            if info['status'] == 'waiting':
                # أول رد للبوت يتم تجاهله
                user_state[user_id]['status'] = 'ready'
                return
            elif info['status'] == 'ready':
                # الرد الثاني يحتوي على الملف الصوتي
                if event.audio:
                    await l313l.send_file(user_id, event.audio)
                else:
                    await l313l.send_message(user_id, f"❌ لم يتم العثور على ملف صوتي لـ: {info['input_text']}")
                # إزالة حالة المستخدم بعد الإرسال
                user_state.pop(user_id)
