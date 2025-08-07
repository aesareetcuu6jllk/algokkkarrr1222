import asyncio
from telethon import events
from telethon.tl.functions.contacts import AddContactRequest
from telethon.errors import UserPrivacyRestrictedError
from JoKeRUB import l313l  # ← تأكد من المسار الصحيح

# الكلمات المفتاحية
KEYWORDS = [
    'محظور', 'محضور',
    'ضيف', 'ضيفني',
    'جهه', 'جه',
    'خلي',
    'دز',
    'ضيف جهه',
    'ضيف جه',
    'ماكدر محظور'
]

# حالة التفعيل
guest_mode_enabled = True

@l313l.on(events.NewMessage)
async def group_reply_handler(event):
    global guest_mode_enabled

    if not event.is_group:
        return

    msg_text = event.raw_text.lower().strip()

    # أوامر تفعيل وتعطيل (تُنفذ فقط إذا الشخص كاتبها مباشرة بدون رد)
    if msg_text == "تفعيل الضيف" and not event.is_reply:
        if (await event.get_sender()).is_self:
            guest_mode_enabled = True
            await event.reply("✅ تم تفعيل أوامر الضيف.")
        return

    if msg_text == "تعطيل الضيف" and not event.is_reply:
        if (await event.get_sender()).is_self:
            guest_mode_enabled = False
            await event.reply("❌ تم تعطيل أوامر الضيف.")
        return

    if not guest_mode_enabled:
        return

    # لازم تكون رد على رسالة البوت نفسه
    if not event.is_reply:
        return

    reply_msg = await event.get_reply_message()
    me = await l313l.get_me()
    if reply_msg.sender_id != me.id:
        return

    # فحص الكلمات المفتاحية
    if not any(keyword in msg_text for keyword in KEYWORDS):
        return

    sender = await event.get_sender()

    try:
        # إضافة لجهات الاتصال
        await l313l(AddContactRequest(
            id=sender.id,
            first_name=sender.first_name or "",
            last_name=sender.last_name or "",
            phone="",
            add_phone_privacy_exception=True
        ))

        await event.reply("ضفتك يروحي راسلني ")

    except UserPrivacyRestrictedError:
        await event.reply("❌ ما أقدر أضيفك بسبب إعدادات الخصوصية.")
    except Exception as e:
        print(f"[❌] خطأ أثناء الإضافة أو الإرسال: {e}")

