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
        match = re.match(ENABLE_PATTERN, msg_text)
        if match:
            new_chat = extract_chat_identifier(match.group(1))
            if new_chat not in target_chats:
                target_chats.append(new_chat)
            await event.reply(f"✅ تم تفعيل المراقبة على: {new_chat}")
            return

        match = re.match(DISABLE_PATTERN, msg_text)
        if match:
            chat_to_remove = match.group(1).strip()
            if chat_to_remove:
                chat_to_remove = extract_chat_identifier(chat_to_remove)
                if chat_to_remove in target_chats:
                    target_chats.remove(chat_to_remove)
                    await event.reply(f"❌ تم تعطيل المراقبة على: {chat_to_remove}")
                else:
                    await event.reply(f"⚠️ هذا الكروب غير مفعّل: {chat_to_remove}")
            else:
                target_chats.clear()
                sent_users.clear()
                await event.reply("❌ تم تعطيل المراقبة على كل الكروبات.")
            return

    if not target_chats:
        return

    # تحقق من الكروب المفعّل
    try:
        chat = await event.get_chat()
        chat_identifier = str(chat.id) if not chat.username else chat.username
        if chat_identifier not in target_chats:
            return
    except Exception:
        return

    # نرسل فقط إذا عنده username
    if sender.username:
        username = f"@{sender.username}"
        if username in sent_users:
            return
        sent_users.add(username)

        try:
            await l313l.send_message("me", username)
            print(f"[✅] أرسل: {username}")
        except Exception as e:
            print(f"[❌] خطأ أثناء الإرسال: {e}")
