import cloudscraper
from telethon import events
from JoKeRUB import l313l

@l313l.on(events.NewMessage(pattern=r'^\.يوزر(?:\s+@?(\w+))?$'))
async def frag_checker(event):
    username = event.pattern_match.group(1)
    if not username:
        await event.reply("📝 أرسل الأمر هكذا:\n`.يوزر @username`")
        return

    url = f"https://fragment.com/username/{username}"
    scraper = cloudscraper.create_scraper()

    try:
        response = scraper.get(url)
        html = response.text.lower()

        if response.status_code == 404:
            await event.reply(f"🟨 `{username}` غير موجود في Fragment\n↪️ **ملكية أو مستخدم عادي**")
        elif "buy" in html or "price" in html:
            await event.reply(f"✅ `{username}` متاح للبيع\n↪️ **منصة (أخضر)**")
        elif "sold" in html or "was sold" in html:
            await event.reply(f"🟥 `{username}` تم بيعه\n↪️ **منصة (أحمر)**")
        else:
            await event.reply(f"⚠️ `{username}` موجود لكن الحالة غير معروفة.")
    except Exception as e:
        await event.reply(f"❌ خطأ أثناء الاتصال:\n`{e}`")
