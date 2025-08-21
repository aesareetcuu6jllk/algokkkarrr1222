from telethon import events, types
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/sekknft"

@l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK, pattern=r"^يوت\s+(.*)"))
async def auto_yt(event):
    input_text = event.pattern_match.group(1)
    user_id = event.sender_id

    # المرحلة الأولى: اختيار تلقائي
    stage1_choice = "اختيار 1"

    # المرحلة الثانية: اختيار تلقائي ملف صوتي
    stage2_choice = "ملف صوتي"

    # إرسال البحث للقروب (يمكن القروب يحتوي ملفات صوتية مرتبطة)
    await l313l.send_message(CHECK_GROUP_LINK, f"يوت {input_text} {stage1_choice} {stage2_choice}")

    # البحث في القروب عن أول رسالة تحتوي الملف الصوتي بعد البحث
    async for msg in l313l.iter_messages(CHECK_GROUP_LINK, limit=50):
        if msg.audio and input_text in (msg.message or ""):
            # إرسال الملف الصوتي للمستخدم مباشرة
            await l313l.send_file(user_id, msg.audio)
            return

    # إذا لم يوجد ملف صوتي
    await l313l.send_message(user_id, f"❌ لم يتم العثور على ملف صوتي لـ: {input_text}")
