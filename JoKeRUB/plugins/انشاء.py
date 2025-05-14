from JoKeRUB import l313l
from ..helpers.utils import reply_id

@l313l.on((pattern="زيج$"))
async def _(event):
    try:
        rpl = await reply_id(event)
        url = "https://t.me/SEFHELLAS/312"  # رابط البصمة
        await event.client.send_file(
            event.chat_id,
            url,
            caption="",
            reply_to=rpl
        )
        await event.delete()
    except Exception as e:
        await event.reply(f"خطأ: {e}")
