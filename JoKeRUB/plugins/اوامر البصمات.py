from JoKeRUB import l313l
from telethon import events

@l313l.on(events.NewMessage(pattern=r'^\.اوامر البصمات$', outgoing=True))
async def _(event):
    await event.reply(
        "⦑ قائمة أوامر البصمات 🎧 ⦒\n"
        "★•────────────•★\n"
        "`.بصمات1`\n"
        "`.بصمات2`\n"
        "`.بصمات3`\n"
        "`.بصمات4`\n"
        "`.بصمات5`\n"
        "`.بصمات6`\n"
        "`.بصمات7`\n"
        "`.بصمات8`\n"
        "`.بصمات9`\n"
        "`.بصمات10`\n"
        "`.بصمات11`\n"
        "`.بصمات12`\n"
        "★•────────────•★\n"
        "CH : @HELLASUserBot"
    )
