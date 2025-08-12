from telethon import events
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/+DGe8lA2FvsM4ZTRi"
activated_users = set()
pending_checks = {}

@l313l.on(events.NewMessage(pattern=r"^\.تفعيل\s+فحص\s+اليوزرات$", incoming=True))
async def activate(event):
    activated_users.add(event.sender_id)
    await event.respond(
        f"✅ تم تفعيل الفحص.\n🔗 انضم للمجموعة:\n{CHECK_GROUP_LINK}\n"
        "ثم استخدم الأمر:\n`.يوزر المعرف` أو قم بالرد على رسالة المعرف وأرسل `.يوزر`"
    )

@l313l.on(events.NewMessage(pattern=r"^\.يوزر(?:\s+(\S+))?$", incoming=True))
async def user_check(event):
    user_id = event.sender_id
    if user_id not in activated_users:
        await event.respond("❌ لازم تفعيل فحص اليوزرات بالأمر:\n`.تفعيل فحص اليوزرات`")
        return

    username = None

    # أولاً نحاول ناخذ اليوزر من النص بعد الأمر
    if event.pattern_match.group(1):
        username = event.pattern_match.group(1).strip()
    # إذا ما كان مكتوب مع الأمر، نجرب ناخذ من رسالة الرد
    elif event.is_reply:
        reply_msg = await event.get_reply_message()
        # نفترض اليوزر يكون في نص الرسالة، ناخذ أول كلمة
        # أو ممكن تعدل حسب شكل معرفاتك
        if reply_msg.text:
            words = reply_msg.text.strip().split()
            if words:
                username = words[0]

    if not username:
        await event.respond("❌ لم يتم العثور على معرف للفحص. اكتب `.يوزر المعرف` أو قم بالرد على رسالة تحتوي المعرف ثم أرسل `.يوزر`")
        return

    username = username.lstrip("@+")

    pending_checks[username.lower()] = event.chat_id

    try:
        await l313l.send_message(CHECK_GROUP_LINK, f"فحص {username}")
    except Exception as e:
        await event.respond(f"⚠️ حدث خطأ أثناء الإرسال: {e}")

@l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK))
async def catch_response(event):
    text = event.raw_text.strip()
    text_lower = text.lower()

    if text_lower.startswith("فحص"):
        return

    for username, target_chat in list(pending_checks.items()):
        if username in text_lower:
            try:
                await l313l.send_message(target_chat, f"📩 نتيجة الفحص:\n{text}")
            except Exception:
                pass
            del pending_checks[username]
            break
