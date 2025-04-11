from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.messages import CreateChatRequest
from telethon.tl.types import PeerUser
import config

client = TelegramClient(StringSession(config.STRING_SESSION), config.APP_ID, config.API_HASH)

async def get_or_create_storage_group():
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.name == "مجموعة التخزين":
            print("تم العثور على مجموعة التخزين.")
            return dialog.entity

    # إذا ما لقاها، ينشئ وحدة جديدة
    try:
        me = await client.get_me()
        result = await client(CreateChatRequest(
            users=[me.username],
            title="مجموعة التخزين"
        ))
        print("تم إنشاء مجموعة التخزين.")
        return result.chats[0]
    except Exception as e:
        print("فشل إنشاء مجموعة التخزين:", e)
        return None

@client.on(events.NewMessage(incoming=True))
async def forward_to_storage_group(event):
    if isinstance(event.peer_id, PeerUser):
        sender = await event.get_sender()
        if not sender.bot:
            print(f"استلمت رسالة من {sender.first_name}")
            storage_group = await get_or_create_storage_group()
            if storage_group:
                try:
                    await client.forward_messages(storage_group.id, event.message)
                    print("تمت إعادة توجيه الرسالة.")
                except Exception as e:
                    print("فشل في توجيه الرسالة:", e)
            else:
                print("ماكو مجموعة تخزين.")

async def main():
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
