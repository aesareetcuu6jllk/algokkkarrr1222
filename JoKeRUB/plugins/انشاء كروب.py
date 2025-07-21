from telethon import events
from telethon.tl import functions, types
from JoKeRUB import l313l
import requests
import re

@l313l.on(events.NewMessage(pattern=r"\.كروب(?:\s+(https?://t\.me/(joinchat/\S+|\+\S+)))?", outgoing=True))
async def creation_handler(event):
    try:
        group_id = None
        chat = None
        match = None

        # 1. إذا أرسلت رابط مع الأمر
        if event.pattern_match.group(1):
            link = event.pattern_match.group(1)
            match = re.match(r"(https?://t\.me/(joinchat/\S+|\+\S+))", link)

        # 2. إذا رديت على رسالة فيها رابط
        elif event.is_reply:
            reply_msg = await event.get_reply_message()
            match = re.search(r"(https?://t\.me/(joinchat/\S+|\+\S+))", reply_msg.text or "")

        if match:
            # استخرج ID الكروب من الرابط
            group_link = match.group(1)
            invite_hash = group_link.split('/')[-1].replace('+', '')

            try:
                joined = await l313l(functions.messages.ImportChatInviteRequest(invite_hash))
                chat = joined.chats[0]
            except Exception:
                invite_info = await l313l(functions.messages.CheckChatInviteRequest(invite_hash))
                if isinstance(invite_info, types.ChatInviteAlready):
                    chat = invite_info.chat
                else:
                    await event.reply("❌ لا يمكن الوصول إلى الكروب.")
                    return

            group_id = chat.id

        else:
            # 3. لم يتم تقديم رابط، نستخدم المجموعة الحالية
            entity = await event.get_chat()
            if isinstance(entity, (types.Chat, types.Channel)):
                group_id = entity.id
                chat = entity
            else:
                await event.reply("❌ لا يمكن تحديد المجموعة.")
                return

        # إرسال الطلب إلى الـ API
        url = f"http://145.223.80.56:5016/date?id={group_id}"
        response = requests.get(url)

        if response.status_code == 200 and response.text.strip():
            name = chat.title if hasattr(chat, 'title') else "?"
            await event.reply(f"📅 تاريخ إنشاء المجموعة:\n• الاسم: {name}\n• ID: `{group_id}`\n• التاريخ: {response.text.strip()}")
        else:
            await event.reply("❌ لم أستطع جلب تاريخ الإنشاء من السيرفر.")

    except Exception as e:
        await event.reply(f"⚠️ خطأ:\n`{str(e)}`")
