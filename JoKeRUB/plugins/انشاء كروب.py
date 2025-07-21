from telethon import events
from JoKeRUB import l313l  # تأكد أن l313l هو client الصحيح
import requests
import re

@l313l.on(events.NewMessage(pattern=r"\.كروب", outgoing=True))
async def creation_handler(event):
    try:
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            # استخراج الرابط من الرسالة التي تم الرد عليها
            match = re.search(r"(https?://t\.me/(joinchat/\S+|\+\S+))", reply_msg.text)
            if not match:
                await event.reply("❌ لم يتم العثور على رابط كروب في الرسالة.")
                return

            group_link = match.group(1)

            # محاولة الانضمام المؤقت للكروب والحصول على ID
            joined = await l313l(functions.messages.ImportChatInviteRequest(group_link.split('/')[-1].replace('+', '')))
            chat = joined.chats[0] if joined.chats else None

            if not chat:
                await event.reply("❌ لم أستطع استخراج معلومات الكروب.")
                return

            group_id = chat.id

        else:
            # إذا لم تكن هناك رسالة فيها رابط
            await event.reply("❌ يجب الرد على رسالة تحتوي على رابط كروب.")
            return

        # طلب معلومات الإنشاء من API خارجي
        url = f"http://145.223.80.56:5016/date?id={group_id}"
        response = requests.get(url)

        if response.status_code == 200 and response.text.strip():
            await event.reply(f"📅 تاريخ إنشاء الكروب:\n{response.text.strip()}")
        else:
            await event.reply("❌ لم أستطع جلب تاريخ الإنشاء أو لا توجد بيانات.")

    except Exception as e:
        await event.reply(f"⚠️ خطأ:\n`{str(e)}`")
