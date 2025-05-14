from JoKeRUB import l313l

# رابط البصمة (ثابت داخل الكود)
URL = "https://t.me/SEFHELLAS/312"  # غيره حسب الرابط إلي تريده

# دالة لجلب reply_id إذا موجود
async def reply_id(event):
    if event.reply_to_msg_id:
        return event.reply_to_msg_id
    return None

@l313l.on((pattern="زيج$"))
async def send_zig_file(event):
    reply = await reply_id(event)

    try:
        await event.client.send_file(
            event.chat_id,
            URL,
            caption="",
            reply_to=reply
        )
    except Exception as e:
        await event.reply(f"حدث خطأ:\n{e}")

    await event.delete()
