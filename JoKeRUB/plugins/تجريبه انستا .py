from JoKeRUB import l313l
from telethon import events
import requests

INSTAGRAM_INFO_TEMPLATE = """
✨ معلومات حساب إنستا:

👤 الاسم: {name}
👥 المتابعون: {followers}
👣 المتابعون: {following}
📝 عدد المنشورات: {posts}
📖 الوصف: {bio}

🔗 رابط الحساب: https://instagram.com/{username}
"""

def format_instagram_info(data, username):
    return INSTAGRAM_INFO_TEMPLATE.format(
        name=data.get('name', 'غير متوفر'),
        followers=data.get('followers', 'غير متوفر'),
        following=data.get('following', 'غير متوفر'),
        posts=data.get('posts', 'غير متوفر'),
        bio=data.get('bio', 'غير متوفر'),
        username=username
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
            msg = format_instagram_info(data, username)
            await wait.edit(msg)
        else:
            await wait.edit("❌ لم أستطع جلب معلومات الحساب.")
    except Exception as e:
        print(f"خطأ جلب معلومات إنستغرام: {e}")
        await wait.edit("❌ حدث خطأ أثناء جلب المعلومات.")
