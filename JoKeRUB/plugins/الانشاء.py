from telethon import events
from JoKeRUB import l313l  # تأكد أن l313l هو client من telethon
import requests

@l313l.on(events.NewMessage(pattern=r"\.الانشاء", outgoing=True))
async def creation_handler(event):
    try:
        # جلب معرف المستخدم: من الرسالة التي تم الرد عليها أو من المرسل الأصلي
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
        else:
            user_id = event.sender_id

        url = f"http://145.223.80.56:5016/date?id={user_id}"
        response = requests.get(url)

        if response.status_code == 200 and response.text.strip():
            await event.reply(f"📅 تاريخ الإنشاء:\n{response.text.strip()}")
        else:
            await event.reply("❌ لم أستطع جلب تاريخ الإنشاء أو لا توجد بيانات.")
    except Exception as e:
        await event.reply(f"❌ حدث خطأ غير متوقع:\n`{str(e)}`")
