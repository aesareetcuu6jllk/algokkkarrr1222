from telethon import events
import aiohttp
from JoKeRUB import l313l

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.يوزر\s+@?(\w+)"))
async def fragment_checker(event):
    username = event.pattern_match.group(1)
    url = f"https://fragment.com/{username}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                html = await resp.text()

        if "Buy" in html or "buy" in html:
            msg = f"✅ اليوزر [@{username}](https://t.me/{username}) **معروض للبيع على المنصة.**"
        elif "Auction ends" in html or "auction" in html:
            msg = f"🔶 اليوزر [@{username}](https://t.me/{username}) **موجود في مزاد على المنصة.**"
        elif "Sold" in html or "sold" in html:
            msg = f"❌ اليوزر [@{username}](https://t.me/{username}) **تم بيعه على المنصة.**"
        else:
            msg = f"❌ اليوزر [@{username}] **غير موجود على منصة Fragment.**"

        await event.reply(msg, link_preview=False)

    except Exception as e:
        await event.reply(f"⚠️ حصل خطأ أثناء الفحص:\n`{str(e)}`")

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.يوزر$"))
async def no_username(event):
    await event.reply("❌ الرجاء كتابة اليوزر بعد الأمر.\nمثال: `.يوزر @ahmad`")

