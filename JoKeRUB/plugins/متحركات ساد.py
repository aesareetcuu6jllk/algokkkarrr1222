from telethon import events
from JoKeRUB.utils import admin_cmd
from JoKeRUB import l313l
from . import *

plugin_category = "extra"

@l313l.ar_cmd(pattern="س1$", command=("س1", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    lMl10l = await reply_id(event)
    if sad:
        await event.client.send_file(event.chat_id, sad, reply_to=lMl10l)

@l313l.ar_cmd(pattern="س2$", command=("س2", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    leo = await reply_id(event)
    if sad2:
        await event.client.send_file(event.chat_id, sad2, reply_to=leo)

@l313l.ar_cmd(pattern="س3$", command=("س3", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    sic_id = await reply_id(event)
    if sad3:
        await event.client.send_file(event.chat_id, sad3, reply_to=sic_id)

@l313l.ar_cmd(pattern="س4$", command=("س4", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    if sad4:
        await event.client.send_file(event.chat_id, sad4, reply_to=reply_to_id)

@l313l.ar_cmd(pattern="س5$", command=("س5", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    if sad5:
        await event.client.send_file(event.chat_id, sad5, reply_to=reply_to_id)

@l313l.ar_cmd(pattern="س6$", command=("س6", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    if sad6:
        await event.client.send_file(event.chat_id, sad6, reply_to=reply_to_id)

@l313l.ar_cmd(pattern="س7$", command=("س7", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    if sad7:
        await event.client.send_file(event.chat_id, sad7, reply_to=reply_to_id)

@l313l.ar_cmd(pattern="س8$", command=("س8", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    if sad8:
        await event.client.send_file(event.chat_id, sad8, reply_to=reply_to_id)

@l313l.ar_cmd(pattern="س9$", command=("س9", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    if sad9:
        await event.client.send_file(event.chat_id, sad9, reply_to=reply_to_id)
