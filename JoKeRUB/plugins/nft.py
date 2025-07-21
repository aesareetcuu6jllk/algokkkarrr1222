from JoKeRUB import l313l
from telethon import events
import aiohttp

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.يوزر\s+@?(\w+)$"))
async def check_fragment_user(event):
    username = event.pattern_match.group(1)
    url = f"https://fragment.com/{username}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                status_code = response.status
                html = await response.text()

        if status_code == 200:
            if "Buy" in html or "buy" in html:
                msg = f"✅ اليوزر [@{username}](https://t.me/{username}) **معروض للبيع على Fragment.**"
            elif "Auction ends" in html or "auction" in html:
                msg = f"🔶 اليوزر [@{username}](https://t.me/{username}) **في مزاد حالياً على Fragment.**"
            elif "Sold" in html or "sold" in html:
                msg = f"❌ اليوزر [@{username}](https://t.me/{username}) **تم بيعه على Fragment.**"
            else:
                msg = f"✅ اليوزر [@{username}] **الصفحة موجودة ولكن حالته غير واضحة.**"
        elif status_code == 404:
            msg = f"❌ اليوزر [@{username}] غير موجود على منصة Fragment."
        else:
            msg = f"⚠️ لا يمكن تحديد الحالة (كود: {status_code})"

        await event.reply(msg, link_preview=False)

    except Exception as e:
        await event.reply(f"❌ خطأ أثناء الفحص:\n`{str(e)}`")

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.يوزر$"))
async def empty_user(event):
    await event.reply("❌ الرجاء كتابة اليوزر بعد الأمر.\nمثال: `.يوزر @username`")

