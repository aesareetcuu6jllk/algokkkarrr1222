from JoKeRUB import l313l
from ..helpers.utils import reply_id  # تأكد أنها موجودة

# رابط ثابت
URL = "https://t.me/SEFHELLAS/312"  # غيره إذا تريد

@l313l.on((pattern="زيج$"))
async def _(event):
    rpl = await reply_id(event)
    try:
        await event.client.send_file(
            event.chat_id,
            URL,
            caption="",
            reply_to=rpl
        )
    except Exception as e:
        await event.reply(f"حدث خطأ:\n{e}")
    await event.delete()
