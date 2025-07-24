from JoKeRUB import l313l
from telethon import events
import requests
import aiohttp
import os

@l313l.on(events.NewMessage(pattern=r'^\.انستا معلومات\s+(\S+)$', outgoing=True))
async def insta_info_handler(event):
    username = event.pattern_match.group(1).strip()
    wait = await event.reply("⏳ جارٍ جلب معلومات الحساب...")

    try:
        api_url = f"http://145.223.80.56:5091/instagram_info?username={username}"
        res = requests.get(api_url)
        res.raise_for_status()
        data = res.json()

        if not data or "username" not in data:
            return await wait.edit("❌ لم أستطع جلب معلومات الحساب.")

        # تحميل صورة البروفايل
        pic_url = data.get("profile_pic_url_hd") or data.get("profile_pic_url")
        img_path = "insta_profile.jpg"

        async with aiohttp.ClientSession() as session:
            async with session.get(pic_url) as resp:
                if resp.status == 200:
                    with open(img_path, "wb") as f:
                        f.write(await resp.read())

        # تجهيز الوصف (caption)
        caption = f"""
👤 الاسم: {data.get('full_name', 'غير متوفر')}
📛 اليوزر: @{data.get('username', 'غير متوفر')}
👥 المتابعين: {data.get('follower_count', 'غير متوفر')}
➡️ يتابع: {data.get('following_count', 'غير متوفر')}
📝 المنشورات: {data.get('media_count', 'غير متوفر')}
📖 النبذة: {data.get('bio', 'لا يوجد')}

🔗 https://instagram.com/{data.get('username')}
"""

        # إرسال الصورة مع الوصف في caption
        await l313l.send_file(
            event.chat_id,
            img_path,
            caption=caption,
            reply_to=event.id
        )

        os.remove(img_path)
        await wait.delete()

    except Exception as e:
        print(f"خطأ: {e}")
        await wait.edit("❌ حدث خطأ أثناء جلب البيانات.")

