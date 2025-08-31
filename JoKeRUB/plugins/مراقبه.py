import asyncio
import re
from telethon import events
from JoKeRUB import l313l  # ← تأكد من المسار الصحيح

monitor_enabled = True
target_chats = []       # قائمة الكروبات المفعلة
sent_users = set()      # لتخزين اليوزرات المرسلة وتجنب التكرار

ENABLE_PATTERN = r"^\.تفعيل مراقبة\s+(.+)$"
DISABLE_PATTERN = r"^\.تعطيل مراقبة\s*(.*)$"

def extract_chat_identifier(text: str):
    text = text.strip()
    # رابط عام
    if text.startswith("https://t.me/") and not "/c/" in text:
        return text.replace("https://t.me/", "").strip()
    # رابط خاص
    if "t.me/c/" in text:
        match = re.search(r"t\.me/c/(\d+)", text)
        if match:
            return f"-100{match.group(1)}"
    # ID مباشر
    if text.startswith("-100"):
        return text
    # username مباشر
    return text

@l313l.on(events.NewMessage)
async def monitor_handler(event):
    global target_chats, sent_users

    msg_text = event.raw_text.strip()
    sender = await event.get_sender()
    if not sender:
        return

    # أوامر التفعيل/التعطيل من صاحب الحساب فقط
    if sender.is_self:
        # تفعيل كروب جديد
        match = re.match(ENABLE_PATTERN, msg_text)
        if match:
            new_chat = extract_chat_identifier(match.group(1))
            if new_chat not in target_chats:
                target_chats.append(new_chat)
            await event.reply(f"✅ تم تفعيل المراقبة على: {new_chat}")
            return

        # تعطيل كروب محدد أو الكل
        match = re.match(DISABLE_PATTERN, msg_text)
        if match:
            chat_to_remove = match.group(1).strip()
            if chat_to_remove:  # تعطيل كروب معين
                chat_to_remove = extract_chat_identifier(chat_to_remove)
                if chat_to_remove in target_chats:
                    target_chats.remove(chat_to_remove)
                    await event.reply(f"❌ تم تعطيل المراقبة على: {chat_to_remove}")
                else:
                    await event.reply(f"⚠️ هذا الكروب غير مفعّل: {chat_to_remove}")
            else:  # تعطيل الكل
                target_chats.clear()
                sent_users.clear()  # نعيد تعيين سجل اليوزرات
                await event.reply("❌ تم تعطيل المراقبة على كل الكروبات.")
            return

    # إذا ما مفعلة أي كروب، نرجع
    if not target_chats:
        return

    # نتحقق أن الرسالة من كروب مفعّل
    try:
        chat = await event.get_chat()
        chat_username = getattr(chat, "username", None)
        chat_id = str(chat.id)
        if chat_id not in target_chats and chat_username not in target_chats:
            return
    except Exception:
        return

    # نرسل username أو id فقط إذا ما أرسل من قبل
    username = f"@{sender.username}" if sender.username else f"id:{sender.id}"
    if username in sent_users:
        return

    sent_users.add(username)

    try:
        await l313l.send_message("me", username)
    except Exception as e:
        print(f"[❌] خطأ أثناء الإرسال: {e}")
