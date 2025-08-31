import asyncio
from telethon import events
from JoKeRUB import l313l  # ← تأكد من المسار الصحيح

target_chats = []       # قائمة الكروبات المفعلة
sent_users = set()      # لتخزين اليوزرات المرسلة وتجنب التكرار

# مراقبة أمر التفعيل
@l313l.on(events.NewMessage(pattern=r"^\.تفعيل احبك$"))
async def activate_monitor(event):
    global target_chats

    sender = await event.get_sender()
    if not sender or not sender.is_self:
        return  # يجب أن يكون الأمر من نفس الحساب

    try:
        chat = await event.get_chat()
        chat_id_str = str(chat.id)
        if chat_id_str not in target_chats:
            target_chats.append(chat_id_str)
            print(f"[✅] تمت إضافة المجموعة للمراقبة: {chat_id_str}")
        else:
            print(f"[⚠️] هذه المجموعة مفعلة مسبقًا: {chat_id_str}")
    except Exception as e:
        print(f"[❌] حدث خطأ أثناء تفعيل المراقبة: {e}")

# مراقبة الرسائل الجديدة في المجموعات المفعلة
@l313l.on(events.NewMessage)
async def monitor_messages(event):
    global target_chats, sent_users

    if not target_chats:
        return

    try:
        chat = await event.get_chat()
        chat_id_str = str(chat.id)
        if chat_id_str not in target_chats:
            return
    except Exception:
        return

    sender = await event.get_sender()
    if not sender:
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
