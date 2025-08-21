import re
from telethon import events, Button
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/sekknft"
pending_checks = {}

# المرحلة الأولى: اختيار عام
@l313l.on(events.NewMessage(pattern=r"^.يوت(?:\s+(.*))?"))
async def yt_cmd(event):
    me = await l313l.get_me()
    if event.sender_id != me.id:
        return

    input_text = event.pattern_match.group(1)
    if not input_text:
        reply = await event.get_reply_message()
        if reply:
            input_text = reply.text or ""
        else:
            return await event.reply("❌ يرجى كتابة شيء بعد .يوت أو الرد على رسالة.")

    buttons = [
        [Button.inline("اختيار 1", b"step1_1"), Button.inline("اختيار 2", b"step1_2")],
        [Button.inline("اختيار 3", b"step1_3")]
    ]
    sent_msg = await event.reply("اختر المرحلة الأولى:", buttons=buttons)
    pending_checks[sent_msg.id] = {"stage": 1, "text": input_text}

# التعامل مع الضغط على الأزرار
@l313l.on(events.CallbackQuery)
async def button_handler(event):
    data = event.data.decode("utf-8")
    message_id = event.message.id

    if message_id not in pending_checks:
        return

    info = pending_checks[message_id]
    stage = info["stage"]
    input_text = info["text"]

    if stage == 1:
        # المرحلة الثانية: تحديد نوع المحتوى
        buttons = [
            [Button.inline("ملف صوتي", b"audio"), Button.inline("مقطع فيديو", b"video")]
        ]
        await l313l.send_message(event.sender_id, f"مرحلة 1: {data}\nاختر نوع المحتوى:", buttons=buttons)
        info["stage"] = 2
        info["stage1_choice"] = data

    elif stage == 2:
        # المرحلة النهائية: إرسال المحتوى مباشرة
        await l313l.send_message(event.sender_id, f"تم اختيارك النهائي: {data}\nجاري جلب المحتوى...")
        
        # إرسال طلب للقروب للبحث عن المحتوى بناءً على كل الاختيارات
        query_msg = f"يوت {input_text} {info.get('stage1_choice')} {data}"
        sent = await l313l.send_message(CHECK_GROUP_LINK, query_msg)

        # لاحقًا يمكن إضافة كود لسحب الفيديو أو الصوت تلقائيًا من الرسالة في القروب
        
        pending_checks.pop(message_id)

