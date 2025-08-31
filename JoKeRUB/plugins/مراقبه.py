import asyncio
import re
from telethon import events
from JoKeRUB import l313l  # ← تأكد من المسار الصحيح

target_chats = []       # قائمة الكروبات المفعلة
sent_users = set()      # لتخزين اليوزرات المرسلة وتجنب التكرار

ENABLE_PATTERN = r"^\.تفعيل مراقبة\s+(.+)$"
DISABLE_PATTERN = r"^\.تعطيل مراقبة\s*(.*)$"

def extract_chat_identifier(text: str):
    text = text.strip()
    # ID مباشر أو رابط خاص
    match = re.search(r"(?:https://t\.me/c/|^)(\d+)", text)
    if match:
        return f"-100{match.group(1)}"
    if text.startswith("-100"):
        return text
    return None  # لا يقبل أي شيء آخر

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
            if new_chat and new_chat not in target_chats:
                target_chats.append(new_chat)
                await event.reply(f"✅ تم تفعيل المراقبة على: {new_chat}")
            else:
                await event.reply("⚠️ يجب استخدام ID صحيح أو رابط خاص t.me/c/...")
            return

        match = re.match(DISABLE_PATTERN, msg_text)
        if match:
            chat_to_remove = extract_chat_identifier(match.group(1).strip())
            if chat_to_remove and chat_to_remove in target_chats:
                target_chats.remove(chat_to_remove)
                await event.reply(f"❌ تم تعطيل المراقبة على: {chat_to_remove}")
            else:
                target_chats.clear()
                sent_users.clear()
                await event.reply("❌ تم تعطيل المراقبة على كل الكروبات.")
            return

    if not target_chats:
        return

    # تحقق أن الرسالة من كروب مفعّل
    try:
        chat = await event.get_chat()
        chat_id_str = str(chat.id)
        if chat_id_str not in target_chats:
            return
    except Exception as e:
        print(f"[⚠️] خطأ أثناء الحصول على الكروب: {e}")
        return

    # أرسل username فقط إذا موجود، وإلا اطبع ID في الكونسول
    if sender.username:
        username = f"@{sender.username}"
        if username not in sent_users:
            sent_users.add(username)
            try:
                await l313l.send_message("me", username)
                print(f"[✅] أرسل: {username}")
            except Exception as e:
                print(f"[❌] خطأ أثناء الإرسال: {e}")
    else:
        print(f"[⚠️] المرسل بدون username، ID: {sender.id}")
