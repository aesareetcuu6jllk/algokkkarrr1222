import asyncio
from telethon import events
from JoKeRUB import l313l  # ← تأكد من المسار الصحيح

target_chats = []       # قائمة الكروبات المفعلة
sent_users = set()      # لتخزين اليوزرات المرسلة وتجنب التكرار

@l313l.on(events.NewMessage(pattern=r"^\.تفعيل احبك$"))
async def monitor_handler(event):
    global target_chats, sent_users

    sender = await event.get_sender()
    if not sender:
        return

    # تأكد أن الأمر من صاحب الحساب
    if sender.is_self:
        try:
            chat = await event.get_chat()
            chat_id_str = str(chat.id)
            if chat_id_str not in target_chats:
                target_chats.append(chat_id_str)
                # ✅ تم حذف الرد على الرسالة، فقط يضيف المجموعة للمراقبة
            # لا نرسل أي رسالة
        except Exception as e:
            print(f"[❌] حدث خطأ أثناء تفعيل المراقبة: {e}")
        return

    if not target_chats:
        return

    # تحقق أن الرسالة من مجموعة مفعلة
    try:
        chat = await event.get_chat()
        chat_id_str = str(chat.id)
        if chat_id_str not in target_chats:
            return
    except Exception:
        return

    # أرسل username فقط إذا موجود
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
