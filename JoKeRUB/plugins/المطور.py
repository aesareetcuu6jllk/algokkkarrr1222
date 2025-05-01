from JoKeRUB import l313l
from ..core.managers import edit_or_reply

plugin_category = "البحث"

@l313l.ar_cmd(
    pattern="المطور$",
    command=("المطور", plugin_category),
    info={
        "header": "لعرض معلومات المطور",
        "الاستـخـدام": "{tr}المطور - لعرض معلومات مطور البوت",
    },
)
async def _(event):
    await edit_or_reply(
        event,
        "╭──── • ◈ • ────╮\n"
        "│ 👑 ᴏᴡɴᴇʀ : [@F_Q_1](https://t.me/F_Q_1)\n"
        "│ 🤖 BOT   : [@qvxbot](https://t.me/qvxbot)\n"
        "│ 📡 CH    : [@HELLASUserBot](https://t.me/HELLASUserBot)\n"
        "╰──── • ◈ • ────╯"
    )
