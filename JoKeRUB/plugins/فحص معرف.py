from telethon import events
from JoKeRUB import l313l

# هنا تحط الإيموجي أو الملصق اللي تريده
NAAL_STICKER = "يجيب عليك الانضمام الى الكروب /n https://t.me/+DGe8lA2FvsM4ZTRi /n بعدها استعمل امر  .يوزر + المعرف"

@l313l.on(events.NewMessage(pattern=r"^(?:\.|)نعال$"))
async def send_naal(event):
    # تأكد إنه اللي كتب الرسالة هو صاحب الحساب
    if event.sender_id != l313l.uid:
        return

    try:
        await event.delete()  # حذف رسالتك الأصلية
        
        if event.is_reply:  
            reply_msg = await event.get_reply_message()
            await event.client.send_message(
                event.chat_id,
                NAAL_STICKER,
                reply_to=reply_msg.id  # يرسل كرد على الرسالة اللي انت راد عليها
            )
        else:
            await event.client.send_message(
                event.chat_id,
                NAAL_STICKER  # يرسل بدون رد
            )
    except Exception as e:
        print("خطأ أثناء إرسال النعال:", e)
