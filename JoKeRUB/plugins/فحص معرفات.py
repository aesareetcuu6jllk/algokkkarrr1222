from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest, SendMessageRequest
from JoKeRUB import l313l

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

    # الانضمام للمجموعة
    try:
        if "+" in CHECK_GROUP_LINK:
            hash_part = CHECK_GROUP_LINK.split("+")[1]
            await l313l(ImportChatInviteRequest(hash_part))
    except Exception:
        pass

    # إرسال أمر الفحص واحفظ الرسالة
    try:
        sent_msg = await l313l.send_message(CHECK_GROUP_LINK, f"فحص {input_text}")
    except Exception as e:
        return await event.reply(f"❌ فشل إرسال الفحص داخل المجموعة:\n{e}")

    # انتظر رد على رسالة sent_msg في القروب لمدة 15 ثانية
    def check_response(resp):
        return resp.is_reply and resp.reply_to_msg_id == sent_msg.id and resp.chat_id == sent_msg.chat_id

    try:
        response = await l313l.wait_for(events.NewMessage(chats=sent_msg.chat_id), timeout=60, func=check_response)
        await event.reply(f"🔎 النتيجة:\n\n{response.text}")
    except Exception:
        await event.reply("⚠️ لم يصل رد من البوت خلال المهلة المحددة.")
