from telethon import events
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/sekknft"

@l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK, pattern=r"^\.يوت\s+(.*)"))
async def yt_auto(event):
    input_text = event.pattern_match.group(1)
    user_id = event.sender_id

    # ===== المرحلة الأولى: أزرار تلقائية =====
    stage1_choices = ["اختيار 1", "اختيار 2", "اختيار 3"]
    stage1_choice = stage1_choices[0]  # يختار البوت تلقائيًا الخيار الأول

    # ===== المرحلة الثانية: نوع المحتوى =====
    stage2_choices = ["ملف صوتي", "مقطع فيديو"]
    stage2_choice = stage2_choices[0]  # يختار البوت تلقائيًا "ملف صوتي"

    # ===== البحث عن الملف الصوتي في القروب =====
    async for msg in l313l.iter_messages(CHECK_GROUP_LINK, limit=50):
        if msg.audio and input_text in (msg.message or ""):
            await l313l.send_file(user_id, msg.audio)  # إرسال الملف الصوتي مباشرة
            return

    # إذا لم يوجد ملف صوتي
    await l313l.send_message(user_id, f"❌ لم يتم العثور على ملف صوتي لـ: {input_text}")
