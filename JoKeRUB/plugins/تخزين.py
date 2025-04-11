from telethon import TelegramClient, events
from telethon.tl.functions.messages import CreateChatRequest
from telethon.tl.types import PeerUser
from JoKeRUB import l313l  # استيراد l313l من JoKeRUB
from config import api_id, api_hash, string_session  # استيراد البيانات من config

from telethon.sessions import StringSession

# استخدام string_session من config.py
client = TelegramClient(StringSession(string_session), api_id, api_hash)

async def get_or_create_storage_group():
    dialogs = await client.get_dialogs()
    storage_group = None
    for dialog in dialogs:
        if dialog.name == "مجموعة التخزين":
            storage_group = dialog.entity
            break

    if not storage_group:
        storage_group = await client(CreateChatRequest(
            users=[], title="مجموعة التخزين"
        ))
        storage_group = storage_group.chats[0]
    return storage_group

@client.on(events.NewMessage(incoming=True))
async def forward_to_storage_group(event):
    if isinstance(event.peer_id, PeerUser):
        sender = await event.get_sender()
        if not sender.bot:
            storage_group = await get_or_create_storage_group()
            await client.forward_messages(storage_group.id, event.message)

client.start()
client.run_until_disconnected()
