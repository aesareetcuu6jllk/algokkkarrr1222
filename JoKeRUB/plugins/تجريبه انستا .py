from JoKeRUB import l313l
from telethon import events
import requests
import re

@l313l.on(events.NewMessage(pattern=r'^\.انستا(?:\s+(https?://[^\s]+))?', outgoing=True))
async def insta_download(event):
    # جلب الرابط من الأمر أو من الرد
    match = event.pattern_match.group(1)
    if match:
        url = match.strip()
    else:
        reply = await event.get_reply_message()
        if reply and re.match(r'https?://(www\.)?(instagram\.com|instagr\.am)/[^\s]+', reply.text):
            url = reply.text.strip()
        else:
            return await event.reply("❌ يرجى إرسال رابط إنستغرام أو الرد عليه.")

    wait = await event.reply("⏳ جارٍ التحميل من إنستغرام...")

    try:
        api_url = f"http://145.223.80.56:5085/download_instagram?url={url}"
        res = requests.get(api_url)
        res.raise_for_status()
        data = res.json()

        if 'download_links' in data and data['download_links']:
            video_url = data['download_links'][0]

            await l313l.send_file(
                entity='me',
                file=video_url,
                caption="✅ تم تحميل الفيديو من إنستغرام."
            )
            await wait.edit("✅ تم إرسال الفيديو إلى الرسائل المحفوظة.")
        else:
            await wait.edit("❌ لم أستطع استخراج روابط الفيديو.")
    except Exception as e:
        print(f"خطأ التحميل من إنستغرام: {e}")
        await wait.edit("❌ حدث خطأ أثناء محاولة التحميل.")
