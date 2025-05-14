#all write Codes By Team Aljoker @jepthon
#By Hussein @lMl10l
import asyncio
import random
import re
import json
import base64
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from asyncio.exceptions import TimeoutError
from telethon import events
from ..sql_helper.memes_sql import get_link, add_link, delete_link, BASE, SESSION, AljokerLink
from telethon.errors.rpcerrorlist import YouBlockedUserError
#ياقائم آل محمد
from JoKeRUB import l313l
from ..helpers.utils import reply_id
plugin_category = "tools"
# الي يخمط ويكول من كتابتي الا امه انيجه وقد اعذر من انذر
@l313l.on(admin_cmd(outgoing=True, pattern="ززيج$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/SEFHELLAS/312"
  await joker313.client.send_file(joker313.chat_id,url,caption="᯽︙ BY : @jepthon 🎀",parse_mode="html")
  await joker313.delete()
