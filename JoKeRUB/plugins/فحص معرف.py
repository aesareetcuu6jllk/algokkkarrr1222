from telethon import events
from JoKeRUB import l313l

GROUP_LINK = "https://t.me/+DGe8lA2FvsM4ZTRi"

@l313l.on(events.NewMessage(pattern=r"^\.تفعيل الفحص$", incoming=True))
async def send_group_link(event):
    await event.respond(f"🔗 هذا هو رابط القروب:\n{GROUP_LINK}")
