import requests
from telethon import events
from JoKeRUB import l313l  # سكربتك

@l313l.on(events.NewMessage(pattern=r'^\.يوزر(?:\s+@?(\w+))?$'))
async def frag_checker(event):
    username = event.pattern_match.group(1)
    if not username:
        await event.reply("📝 أرسل الأمر هكذا:\n`.يوزر @username`")
        return

    url = f"https://fragment.com/username/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(url, headers=headers)

        if r.status_code == 404:
            await event.reply(f"🟨 `{username}` غير موجود في Fragment\n↪️ **ملكية أو مستخدم عادي**")
            return

        if "Buy" in r.text or "price" in r.text:
            await event.reply(f"✅ `{username}` متاح للبيع\n↪️ **منصة (أخضر)**")
        elif "Sold" in r.text or "was sold" in r.text:
            await event.reply(f"🟥 `{username}` تم بيعه\n↪️ **منصة (أحمر)**")
        else:
            await event.reply(f"⚠️ `{username}` موجود لكن الحالة غير معروفة.")
    except Exception as e:
        await event.reply(f"❌ خطأ أثناء الاتصال بـ Fragment:\n`{e}`")

