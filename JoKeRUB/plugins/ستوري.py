from telethon.events import NewMessage
from JoKeRUB import l313l

@l313l("نعال")
async def sandal_cmd(event: NewMessage.Event):
    me = await event.client.get_me()
    if event.sender_id != me.id:
        return  # تجاهل أي شخص غير صاحب الحساب

    await event.respond("🩴🩴")
    await event.delete()

