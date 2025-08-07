import asyncio
from telethon import events
from telethon.tl.functions.contacts import AddContactRequest
from telethon.errors import UserPrivacyRestrictedError
from JoKeRUB import l313l  # ← الكلاينت الجاهز من مشروعك

# الكلمات المفتاحية
KEYWORDS = ['محظور', 'ضيفني', 'جه ضيفني جه', 'محظور ضيف']

@l313l.on(events.NewMessage)
async def group_reply_handler(event):
    # فقط في الكروبات
    if not event.is_group:
        return

    # فقط إذا كانت رد على رسالة الحساب
    if not event.is_reply:
        return

    reply_msg = await event.get_reply_message()
    me = await l313l.get_me()
    if reply_msg.sender_id != me.id:
        return

    msg_text = event.raw_text.lower()

    # التحقق من الكلمات المفتاحية
    if not any(keyword in msg_text for keyword in KEYWORDS):
        return

    sender = await event.get_sender()

    try:
        # إضافة المرسل إلى جهات الاتصال باسمه الحقيقي
        await l313l(AddContactRequest(
            id=sender.id,
            first_name=sender.first_name or "",
            last_name=sender.last_name or "",
            phone="",
            add_phone_privacy_exception=True
        ))

        # الرد عليه بالكروب
        await event.reply("ضفتك، دز هوه شراح يسوي")

        # إرسال رسالة له بالخاص
        await l313l.send_message(sender.id, "دز، ضفتك")

    except UserPrivacyRestrictedError:
        await event.reply("❌ ما أقدر أضيفك بسبب إعدادات الخصوصية.")
    except Exception as e:
        print(f"[❌] خطأ أثناء الإضافة أو الإرسال: {e}")
