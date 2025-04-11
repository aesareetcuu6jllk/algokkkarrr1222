from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.messages import CreateChatRequest
from telethon.tl.types import PeerUser
import config

# إنشاء الكلاينت
client = TelegramClient(StringSession(config.STRING_SESSION), config.app_id, config.api_hash)

# تخزين كاش للكيان
storage_group = None

async def get_or_create_storage_group():
    global storage_group

    if storage_group:
        return storage_group

    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.name == "مجموعة التخزين":
            storage_group = dialog.entity
            return storage_group

    # لا يمكن إنشاء مجموعة بدون مستخدمين، لذلك ننشئ شات مع نفسك أولاً كحل مؤقت
    me = await client.get_me()
    result = await client(CreateChatRequest(
        users=[me.id],  # نضيف نفسك لإنشاء المجموعة
        title="مجموعة التخزين"
    ))

    storage_group = result.chats[0]
    return storage_group

@client.on(events.NewMessage(incoming=True))
async def forward_to_storage_group(event):
    if isinstance(event.peer_id, PeerUser):
        sender = await event.get_sender()
        if not sender.bot:
            group = await get_or_create_storage_group()
            await client.forward_messages(group.id, event.message)

async def main():
    print("تم تسجيل الدخول بنجاح.")
    await client.start()
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
