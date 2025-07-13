from telethon import TelegramClient, events
from youtube_search import YoutubeSearch
import requests, asyncio, os, re
import subprocess

# بيانات حسابك الشخصي
APP_ID = 24347380
API_HASH = "1ad5dea4dfdddfed44df611dcd0d1736"

# إنشاء جلسة (سيطلب منك رقمك أول مرة)
client = TelegramClient("YouTubeSession", APP_ID, API_HASH)

# مجلد التنزيل
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# دالة البحث في يوتيوب
def search_youtube(query):
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        if results:
            return f"https://www.youtube.com/watch?v={results[0]['id']}", results[0]['title']
    except:
        return None, None

# دالة تحميل الصوت MP3
def download_audio(url, title):
    safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
    output_path = f"downloads/{safe_title}.mp3"
    cmd = f'yt-dlp -x --audio-format mp3 -o "{output_path}" "{url}"'
    subprocess.call(cmd, shell=True)
    return output_path if os.path.exists(output_path) else None

# الأمر: .يوتو + الاسم
@client.on(events.NewMessage(pattern=r'^\.يوتو (.+)'))
async def ytdl_handler(event):
    query = event.pattern_match.group(1)
    await event.reply("🔎 يتم البحث عن الفيديو...")

    url, title = search_youtube(query)
    if not url:
        return await event.reply("❌ لم يتم العثور على نتائج.")

    await event.reply("🎧 يتم التحميل الآن...")
    audio_path = download_audio(url, title)
    if not audio_path:
        return await event.reply("❌ فشل تحميل الصوت.")

    await client.send_file(event.chat_id, audio_path, caption=f"🎵 {title}")
    os.remove(audio_path)

# تشغيل العميل
print("✅ تم تشغيل البوت. اكتب .يوتو + الاسم في أي دردشة.")
client.start()
client.run_until_disconnected()
