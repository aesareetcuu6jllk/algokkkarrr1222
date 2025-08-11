from telethon import events
from JoKeRUB import l313l  # غيّرها إذا اسم الكلاينت مختلف

# هنا تحط الإيموجي أو السمايل اللي تريده
NAAL_EMOJI = "🩴"  # مثلا نعال

@l313l.on(events.NewMessage(pattern=r"^\.نعال$"))
async def naal_smile(event):
    try:
        await event.delete()  # حذف رسالتك
        await event.client.send_message(event.chat_id, NAAL_EMOJI)  # إرسال السمايل
    except Exception as e:
        print("خطأ أثناء إرسال النعال:", e)
