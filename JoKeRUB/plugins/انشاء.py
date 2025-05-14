import random
from JoKeRUB import l313l
from ..helpers.utils import reply_id

@l313l.on((pattern="زيج$"))
async def _(event):
    try:
        rl = random.randint(1, 31)
        url = f"https://t.me/SEFHELLAS/312"
        await event.client.send_file(
            event.chat_id,
            url,
            caption="⎉╎ عظم الله لنا ولكم الاجر بهذا المُصاب الجلل 🏴",
            parse_mode="html",
            reply_to=await reply_id(event)
        )
        await event.delete()
    except Exception as e:
        await event.reply(f"🚫 حدث خطأ:\n{e}")

