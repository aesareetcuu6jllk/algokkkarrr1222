from telethon import events
from JoKeRUB.utils import admin_cmd
from JoKeRUB import l313l
from . import *

plugin_category = "extra"

@l313l.ar_cmd(pattern="ك1$", command=("ك1", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    ROZ = await reply_id(event)
    if cute:
        await event.client.send_file(event.chat_id, cute, reply_to=ROZ)

@l313l.ar_cmd(pattern="ك2$", command=("ك2", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    leo = await reply_id(event)
    if cute2:
        await event.client.send_file(event.chat_id, cute2, reply_to=leo)

@l313l.ar_cmd(pattern="ك3$", command=("ك3", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    sic_id = await reply_id(event)
    if cute3:
        await event.client.send_file(event.chat_id, cute3, reply_to=sic_id)

@l313l.ar_cmd(pattern="ك4$", command=("ك4", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    if cute4:
        await event.client.send_file(event.chat_id, cute4, reply_to=reply_to_id)

@l313l.ar_cmd(pattern="ك5$", command=("ك5", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    if cute5:
        await event.client.send_file(event.chat_id, cute5, reply_to=reply_to_id)

@l313l.ar_cmd(pattern="ك6$", command=("ك6", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    if cute6:
        await event.client.send_file(event.chat_id, cute6, reply_to=reply_to_id)

@l313l.ar_cmd(pattern="ك7$", command=("ك7", plugin_category))
async def tmgif(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    if cute7:
        await event.client.send_file(event.chat_id, cute7, reply_to=reply_to_id)
