from telethon import events
from JoKeRUB import l313l

# هنا تحط الإيموجي أو الملصق اللي تريده
NAAL_STICKER = "🩴🩴"  # تقدر تحط رابط ملصق أو إيموجي

@l313l.on(events.NewMessage(pattern=r"^(?:\.|)نعال$"))
async def send_naal(event):
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

NnAAL_STICKER = "هههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههه .متت"
@l313l.on(events.NewMessage(pattern=r"^(?:\.|)ه$"))
async def send_naal(event):
    # يتأكد إنه الرسالة من صاحب الحساب نفسه
    if event.sender_id != l313l.uid:
        return

    try:
        await event.delete()  # حذف رسالتك الأصلية

        if event.is_reply:  
            reply_msg = await event.get_reply_message()
            await event.client.send_message(
                event.chat_id,
                NnAAL_STICKER,
                reply_to=reply_msg.id  # يرسل كرد على الرسالة اللي انت راد عليها
            )
        else:
            await event.client.send_message(
                event.chat_id,
                NnAAL_STICKER  # يرسل بدون رد
            )
    except Exception as e:
        print("خطأ أثناء إرسال النص:", e)
