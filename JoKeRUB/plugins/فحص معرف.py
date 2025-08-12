from telethon import events
from JoKeRUB import l313l

GROUP_LINK = "https://t.me/+DGe8lA2FvsM4ZTRi"

@l313l.on(events.NewMessage(pattern=r"^\.رابط$", incoming=True))
async def send_group_link(event):
    # يرسل الرد في نفس مكان الرسالة (خاص أو مجموعة)
    await event.respond(f"🔗 هذا هو رابط القروب:\n{GROUP_LINK}")
