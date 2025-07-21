import re
import requests
from telethon import events
from JoKeRUB import l313l

client = l313l.client  # الجلسة من مكتبتك

async def check_user_exists(username: str) -> bool:
    try:
        await client.get_entity(username)
        return True
    except Exception:
        return False

@client.on(events.NewMessage(pattern=r'^\.يوزر\s+(@?\w+)$'))
async def user_check(event):
    user = event.pattern_match.group(1).lstrip("@")
    await event.reply(f"🔎 جاري فحص @{user} ...")

    exists = await check_user_exists(user)

    url = f"https://fragment.com/username/{user}"
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            html = resp.text

            status = "🟢 منصّة (NFT)" if 'tm-status-taken' not in html else "🟡 ملكية فقط"

            usd_match = re.search(r'<span class="js-bid_usd_value">([^<]+)<\/span>', html)
            usd_value = usd_match.group(1) if usd_match else "❌"

            ton_match = re.search(r'<div class="table-cell-value tm-value icon-before icon-ton">\s*([\d,]+)\s*<\/div>', html)
            ton_value = ton_match.group(1) if ton_match else "❌"

            result = (
                f"🧾 نتيجة فحص @{user}:\n"
                f"▪️ الحالة: {status}\n"
                f"▪️ السعر: {ton_value} TON ~ {usd_value}$\n"
                f"▪️ متوفر على تيليجرام: {'✅ نعم' if exists else '❌ لا'}\n"
                f"\n🔗 https://fragment.com/username/{user}"
            )
            await event.reply(result)
        else:
            await event.reply("⚠️ لم أتمكن من الوصول إلى fragment.com.")
    except Exception as e:
        await event.reply(f"❌ حدث خطأ أثناء الفحص: {e}")

