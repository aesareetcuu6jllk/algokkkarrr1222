import re
import requests
import asyncio
from telethon import events
from JoKeRUB import l313l

client = l313l.client  # Telethon async client

async def check_user_exists(username: str) -> bool:
    try:
        await client.get_entity(username)
        return True
    except Exception:
        return False

@client.on(events.NewMessage(pattern=r'^\.يوزر\s+(@?\w+)$'))
async def user_check(event):
    user = event.pattern_match.group(1).lstrip("@")
    await event.reply(f"⏳ جاري الفحص @{user} ...")

    exists = await check_user_exists(user)

    url = f"https://fragment.com/username/{user}"
    resp = requests.get(url)
    if resp.status_code == 200:
        html = resp.text
        status = "NFT" if '<span class="tm-section-header-status tm-status-taken">Taken</span>' not in html else "ليس NFT"

        usd_match = re.search(r'<span class="js-bid_usd_value">([^<]+)<\/span>', html)
        usd_value = usd_match.group(1) if usd_match else "لا يوجد"

        ton_match = re.search(r'<div class="table-cell-value tm-value icon-before icon-ton">\s*([\d,]+)\s*<\/div>', html)
        bid_amount = f"Ton: {ton_match.group(1)} | USD: {usd_value}$" if ton_match else "لا يوجد"

        text = (
            f"✅ نتيجة الفحص لـ @{user}:\n"
            f"- الحالة: {status}\n"
            f"- السعر: {bid_amount}\n"
            f"- موجود على تيليجرام: {'نعم' if exists else 'لا'}\n"
            f"\n🔗 الرابط: {url}"
        )
        await event.reply(text)
    else:
        await event.reply("❌ لم أتمكن من جلب بيانات من fragment.com.")

if __name__ == "__main__":
    print("Bot started...")
    client.run_until_disconnected()
