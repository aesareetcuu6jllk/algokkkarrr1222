from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest, SendMessageRequest
from JoKeRUB import l313l

# رابط الدعوة للمجموعة الخاصة بالفحص
CHECK_GROUP_LINK = "https://t.me/+DGe8lA2FvsM4ZTRi"

@l313l.on(events.NewMessage(pattern=r"^.يوزر(?:\s+(.*))?"))
async def sandal_cmd(event: events.NewMessage.Event):
    input_text = event.pattern_match.group(1)
    if not input_text:
        reply = await event.get_reply_message()
        if reply and reply.sender:
            username = reply.sender.username
            if not username:
                return await event.reply("❌ المستخدم لا يملك يوزر.")
            input_text = f"@{username}"
        else:
            return await event.reply("❌ يرجى كتابة المعرف أو الرد على رسالة.")

    # الانضمام للمجموعة من خلال الرابط
    try:
        if "+" in CHECK_GROUP_LINK:
            hash_part = CHECK_GROUP_LINK.split("+")[1]
            await l313l(ImportChatInviteRequest(hash_part))
    except Exception:
        pass

    try:
        await l313l(SendMessageRequest(peer=CHECK_GROUP_LINK, message=f"فحص {input_text}"))
    except Exception as e:
        return await event.reply(f"❌ فشل إرسال الفحص داخل المجموعة:\n{e}")

    try:
        async for msg in l313l.iter_messages(CHECK_GROUP_LINK, limit=10):
            if msg.text and input_text in msg.text:
                return await event.reply(f"🔎 النتيجة:\n\n{msg.text}")
        await event.reply("❌ لم يتم العثور على رد من البوت.")
    except Exception as e:
        await event.reply(f"❌ حدث خطأ أثناء انتظار الرد:\n{e}")

