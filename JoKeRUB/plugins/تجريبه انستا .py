from JoKeRUB import l313l
from telethon import events
import requests

INSTAGRAM_INFO_TEMPLATE = """
✨ معلومات حساب إنستا:

👤 الاسم: {full_name}
👥 المتابعون: {follower_count}
👣 المتابعون: {following_count}
📝 عدد المنشورات: {media_count}
📖 الوصف: {bio}

🔗 رابط الحساب: https://instagram.com/{username}
"""

def format_instagram_info(data):
    return INSTAGRAM_INFO_TEMPLATE.format(
        full_name=data.get('full_name', 'غير متوفر'),
        follower_count=data.get('follower_count', 'غير متوفر'),
        following_count=data.get('following_count', 'غير متوفر'),
        media_count=data.get('media_count', 'غير متوفر'),
        bio=data.get('bio', 'غير متوفر'),
        username=data.get('username', 'غير متوفر')
    )

@l313l.on(events.NewMessage(pattern=r'^\.انستا معلومات\s+(\S+)$', outgoing=True))
async def insta_info_handler(event):
    username = event.pattern_match.group(1).strip()
    wait = await event.reply("⏳ جارٍ جلب معلومات الحساب...")

    try:
        api_url = f"http://145.223.80.56:5091/instagram_info?username={username}"
        res = requests.get(api_url)
        res.raise_for_status()
        data = res.json()

        if data:
            msg = format_instagram_info(data)
            await wait.edit(msg)
        else:
            await wait.edit("❌ لم أستطع جلب معلومات الحساب.")
    except Exception as e:
        print(f"خطأ جلب معلومات إنستغرام: {e}")
        await wait.edit("❌ حدث خطأ أثناء جلب المعلومات.")
