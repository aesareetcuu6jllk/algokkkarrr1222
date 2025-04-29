from JoKeRUB import l313l
import random
import glob
import os
from yt_dlp import YoutubeDL
from telethon.tl.types import Message

plugin_category = "البوت"

def get_cookies_file():
    folder_path = f"{os.getcwd()}/rcookies"
    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
    if not txt_files:
        raise FileNotFoundError("لا يوجد ملفات كوكيز في المجلد المحدد.")
    return random.choice(txt_files)

@l313l(pattern='.بحث3 (.*)')
async def _(event: Message):
    song_name = event.pattern_match.group(1)
    await event.reply(f"🕵️‍♂️ جارٍ البحث عن الأغنية: **{song_name}**...")

    ydl_opts = {
        "format": "bestaudio/best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quiet": True,
        "cookiefile": get_cookies_file(),
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{song_name}", download=False)
            if not info['entries']:
                await event.reply("❌ لم يتم العثور على أي نتائج.")
                return

            response_message = "🎶 تم العثور على الأغاني التالية:\n"
            for index, entry in enumerate(info['entries'][:5], start=1):
                response_message += f"{index}. {entry['title']}\n"
            response_message += "\n📝 أرسل رقم الأغنية لتحميلها."

            await event.reply(response_message)

            reply = await event.client.wait_for(events.NewMessage(
                chats=event.chat_id,
                from_users=event.sender_id
            ))

            selected_index = int(reply.text.strip()) - 1
            if 0 <= selected_index < len(info['entries']):
                selected_entry = info['entries'][selected_index]
                title = selected_entry['title']
                await event.reply(f"📥 جاري تحميل: **{title}**...")

                ydl.download([selected_entry['webpage_url']])
                filename = f"{title}.mp3"

                await event.client.send_file(event.chat_id, filename)
                os.remove(filename)
            else:
                await event.reply("⚠️ رقم غير صالح.")
    except Exception as e:
        await event.reply(f"🚫 حدث خطأ أثناء البحث عن الأغنية:\n`{str(e)}`")
