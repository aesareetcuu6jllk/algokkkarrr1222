from JoKeRUB import l313l
from telethon import events
import aiohttp

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.يوزر\s+@?(\w+)$"))
async def check_fragment_user(event):
    username = event.pattern_match.group(1)
    url = f"https://fragment.com/{username}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                status_code = response.status
                html = await response.text()

        if status_code == 200:
            if "tgme_username_link" in html or "/cdn-cgi/l/email-protection" in html:
                msg = f"✅ اليوزر [@{username}](https://t.me/{username}) **موجود على المنصة.**"
            elif "auction ends" in html.lower():
                msg = f"🔶 اليوزر [@{username}] **في مزاد على Fragment.**"
            elif "sold" in html.lower():
                msg = f"❌ اليوزر [@{username}] **تم بيعه سابقاً على Fragment.**"
            else:
                msg = f"✅ اليوزر [@{username}] **صفحة موجودة لكن حالته غير واضحة (احتمال معروض).**"
        elif status_code == 404:
            msg = f"❌ اليوزر [@{username}] غير موجود على منصة Fragment."
        else:
            msg = f"⚠️ حالة غير معروفة (status code: {status_code})"

        await event.reply(msg, link_preview=False)

    except Exception as e:
        await event.reply(f"❌ خطأ أثناء الفحص:\n`{str(e)}`")

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.يوزر$"))
async def empty_user(event):
    await event.reply("❌ يرجى كتابة اليوزر بعد الأمر.\nمثال: `.يوزر @joker`")

