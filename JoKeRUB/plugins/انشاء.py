import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from repthon.utils import admin_cmd
from ..helpers.utils import reply_id
from JoKeRUB import l313l

# الي يخمط ويكول من كتابتي الا امه انيجه وقد أعذر من أنذر
# السلام على الحسين وعلى الأرواح التي حلت بفنائك، ولعن الله قاتليك

@l313l.on(admin_cmd(pattern="زيج$"))
async def jepmeme(memejep):
    Rep = await reply_id(memejep)
    url = "https://t.me/SEFHELLAS/312"
    await memejep.client.send_file(
        memejep.chat_id,
        url,
        caption="",
        parse_mode="html",
        reply_to=Rep
    )
    await memejep.delete()
