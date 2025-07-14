from JoKeRUB import l313l
import requests
import random

@l313l.on(events.NewMessage(pattern=r'^\.حساب انستا (.+)$', outgoing=True))
async def insta_info(event):
    username = event.pattern_match.group(1).strip()

    headers = {
        'user-agent': random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
        ]),
        'x-ig-app-id': '936619743392459'
    }
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
    
    try:
        r = requests.get(url, headers=headers)
        data = r.json()
        if r.status_code != 200 or 'user' not in data.get('data', {}):
            return await event.edit(f"❌ الحساب غير موجود: {username}")
        
        user_data = data['data']['user']
        name = user_data.get('full_name', 'N/A')
        bio = user_data.get('biography', 'لا يوجد')
        followers = user_data.get('edge_followed_by', {}).get('count', 0)
        following = user_data.get('edge_follow', {}).get('count', 0)
        verified = "نعم" if user_data.get('is_verified') else "لا"
        private = "نعم" if user_data.get('is_private') else "لا"
        posts = user_data.get('edge_owner_to_timeline_media', {}).get('count', 0)
        pfp = user_data.get('profile_pic_url_hd', '')

        text = f"""
📸 معلومات إنستا: @{username}

• الاسم: {name}
• المتابعين: {followers}
• يتابع: {following}
• المنشورات: {posts}
• خاص؟ {private}
• موثق؟ {verified}
• البايو: {bio}
"""
        if pfp:
            await event.client.send_file(event.chat_id, pfp, caption=text)
        else:
            await event.edit(text)
    except Exception as e:
        await event.edit(f"حدث خطأ: {str(e)}")
