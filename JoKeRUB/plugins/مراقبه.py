import asyncio
import re
from telethon import events
from JoKeRUB import l313l  # ← تأكد من المسار الصحيح

# حالة التفعيل
monitor_enabled = False
target_chat = None  # نخزن هنا الكروب المحدد

# أوامر التفعيل والتعطيل
ENABLE_PATTERN = r"^\.تفعيل مراقبة\s+(.+)$"
DISABLE_COMMANDS = [".تعطيل مراقبة"]

def extract_chat_identifier(text: str):
    """
    يحوّل الرابط أو النص المدخل إلى شكل مناسب (id أو username).
    يقبل:
    - رابط عام: https://t.me/groupname
    - رابط خاص: https://t.me/c/123456789/1
    - آيدي مباشر: -100xxxxxxxxxx
    - يوزر مباشر: groupname
    """
    text = text.strip()

    # رابط عام
    if text.startswith("https://t.me/") and not "/c/" in text:
        return text.replace("https://t.me/", "").strip()

    # رابط خاص (t.me/c/123456789/...)
    if "t.me/c/" in text:
        # نستخرج الرقم
        match = re.search(r"t\.me/c/(\d+)", text)
        if match:
            return f"-100{match.group(1)}"

    # إذا آيدي مباشر
    if text.startswith("-100"):
        return text

    # إذا بس يوزر (مثل groupname)
    return text


@l313l.on(events.NewMessage)
async def monitor_handler(event):
    global monitor_enabled, target_chat

    msg_text = event.raw_text.strip()
    sender = await event.get_sender()

    # أوامر التفعيل والتعطيل (فقط من حسابك)
    if sender and sender.is_self:

        # تفعيل
        match = re.match(ENABLE_PATTERN, msg_text)
        if match and not event.is_reply:
            raw_value = match.group(1).strip()
            target_chat = extract_chat_identifier(raw_value)

            monitor_enabled = True
            await event.reply(f"✅ المراقبة فعّالة على: {target_chat}")
            return

        # تعطيل
        if msg_text in DISABLE_COMMANDS and not event.is_reply:
            monitor_enabled = False
            target_chat = None
            await event.reply("❌ تم تعطيل المراقبة.")
            return

    # إذا ما مفعلة
    if not monitor_enabled or not target_chat:
        return

    # نتحقق أن الرسالة من الكروب المطلوب
    try:
        chat = await event.get_chat()
        chat_username = getattr(chat, "username", None)
        chat_id = chat.id

        if str(chat_id) != str(target_chat) and chat_username != target_chat:
            return
    except Exception:
        return

    # نجيب معلومات المرسل
    sender = await event.get_sender()
    if not sender:
        return

    # فقط اليوزر أو id
    username = f"@{sender.username}" if sender.username else f"id:{sender.id}"

    try:
        await l313l.send_message("me", username)
    except Exception as e:
        print(f"[❌] خطأ أثناء الإرسال: {e}")
