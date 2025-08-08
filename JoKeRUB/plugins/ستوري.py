from telethon.events import NewMessage
from JoKeRUB import l313l  # حسب سورسك

@l313l("نعال")
async def send_sandal_sticker(event: NewMessage.Event):
    await event.client.send_file(
        event.chat_id,
        file="CAACAgUAAxkBAAEBxI5kflUWeB4LLNtnQa8YcFJfiZlLfQACmAADWbv8JXPOnOBpAhZbNAQ",  # آيدي ملصق نعال
        reply_to=event.reply_to_msg_id
    )
    await event.delete()  # يحذف الأمر بعد الإرسال
