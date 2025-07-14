from telethon import TelegramClient, events
from telethon.sessions import StringSession
import requests
import random
import config

client = TelegramClient(StringSession(config.STRING_SESSION), config.APP_ID, config.API_HASH)

@client.on(events.NewMessage(pattern=r'^\.انستا (.+)$'))
async def insta_info(event):
    user = event.pattern_match.group(1).strip()
    headers = {
        'user-agent': random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
        ]),
        'x-ig-app-id': '936619743392459'
    }
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={user}"
    r = requests.get(url, headers=headers)
    if r.status_code != 200 or 'user' not in r.json().get('data', {}):
        return await event.reply(f"❌ الحساب غير موجود: {user}")
    
    data = r.json()['data']['user']
    name = data.get('full_name', 'N/A')
    bio = data.get('biography', 'لا يوجد')
    followers = data.get('edge_followed_by', {}).get('count', 0)
    following = data.get('edge_follow', {}).get('count', 0)
    verified = "نعم" if data.get('is_verified') else "لا"
    private = "نعم" if data.get('is_private') else "لا"
    posts = data.get('edge_owner_to_timeline_media', {}).get('count', 0)
    pfp = data.get('profile_pic_url_hd', '')

    text = f"""
📸 معلومات إنستا: @{user}

• الاسم: {name}
• المتابعين: {followers}
• يتابع: {following}
• المنشورات: {posts}
• خاص؟ {private}
• موثق؟ {verified}
• البايو: {bio}
"""
    if pfp:
        await client.send_file(event.chat_id, pfp, caption=text)
    else:
        await event.reply(text)

client.start()
client.run_until_disconnected()

