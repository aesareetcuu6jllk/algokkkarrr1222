from JoKeRUB import l313l
from telethon import events
import subprocess
import os
import tempfile
import json
import asyncio
import re

# دالة التحميل العامة
async def download_and_send_file(event, url, platform):
    try:
        await event.reply(f"جاري التحميل من {platform}، يرجى الانتظار...")

        with tempfile.TemporaryDirectory() as tmpdir:
            output_template = os.path.join(tmpdir, '%(title)s.%(ext)s')

            try:
                info_command = ['yt-dlp', '--no-warnings', '--dump-json', url]
                info_process = subprocess.run(info_command, capture_output=True, text=True, check=True)
                video_info = json.loads(info_process.stdout)

                if video_info.get('_type') == 'playlist':
                    return await event.reply("❌ لا يمكن تحميل قوائم التشغيل.")

                estimated_filesize = video_info.get('filesize') or video_info.get('filesize_approx')
                if estimated_filesize and estimated_filesize > 2 * 1024 * 1024 * 1024:
                    return await event.reply("❌ الملف أكبر من 2GB!")

                format_selector = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'
                if video_info.get('is_live'):
                    format_selector = 'best[ext=mp4]'
                elif video_info.get('ext') == 'mp3' or video_info.get('acodec') != 'none':
                    format_selector = 'bestaudio/best'

            except Exception:
                return await event.reply("❌ فشل جلب معلومات الفيديو.")

            download_command = [
                'yt-dlp', '--no-warnings', '-f', format_selector,
                '--output', output_template, url
            ]
            subprocess.run(download_command, cwd=tmpdir, capture_output=True, text=True, check=True)

            files = [os.path.join(tmpdir, f) for f in os.listdir(tmpdir)
                     if f.endswith(('.mp4', '.mkv', '.webm', '.mp3', '.m4a', '.ogg', '.wav'))]
            if not files:
                return await event.reply("❌ لم يتم العثور على ملفات.")

            file_path = files[0]
            size = os.path.getsize(file_path)
            if size > 2 * 1024 * 1024 * 1024:
                return await event.reply("❌ الملف كبير جداً ولا يمكن رفعه.")

            await event.reply("⬆️ جاري رفع الملف...")

            ext = os.path.splitext(file_path)[1].lower()
            title = video_info.get('title', 'بدون عنوان')

            if ext in ['.mp4', '.mkv', '.webm']:
                await l313l.send_file('me', file_path, caption=f"🎬 {title}\nمن {platform}")
            else:
                await l313l.send_file('me', file_path, caption=f"🎧 {title}\nمن {platform}")

            await event.reply("✅ تم الإرسال بنجاح!")
    except Exception as e:
        await event.reply(f"❌ خطأ أثناء التحميل: {e}")

# أمر المساعدة
from JoKeRUB import l313l
from telethon import events

@l313l.on(events.NewMessage(pattern=r'^\.اوامر التنزيل$', outgoing=True))
async def download_commands(event):
    await event.reply(
        "**📥 أوامر التنزيل المدعومة:**\n\n"
        "⥾ `.يوتيوب + الرابط` أو الرد على رابط يوتيوب\n"
        "⥾ `.تيكتوك + الرابط` أو الرد على رابط تيك توك\n"
        "⥾ `.انستا + الرابط` أو الرد على رابط إنستغرام\n"
        "⥾ `.فيس + الرابط` أو الرد على رابط فيسبوك\n"
        "⥾ `.تويتر + الرابط` أو الرد على رابط تويتر\n"
        "⥾ `.ساوند + الرابط` أو الرد على رابط ساوندكلاود\n\n"
        "🎬 يتم إرسال الملفات إلى الرسائل المحفوظة (Saved Messages).\n"
        "⚠️ تأكد أن الرابط مباشر لفيديو وليس قائمة تشغيل أو بث مباشر.\n\n"
        "⌔︙المطور : @HELLASUserBot"
    )


# أوامر التحميل
@l313l.on(events.NewMessage(pattern=r"\.تيكتوك(?: (.*))?", outgoing=True))
async def tiktok_cmd(event):
    url = event.pattern_match.group(1) or (await event.get_reply_message()).text.strip()
    await download_and_send_file(event, url, "TikTok")

@l313l.on(events.NewMessage(pattern=r"\.يوتيوب(?: (.*))?", outgoing=True))
async def yt_cmd(event):
    url = event.pattern_match.group(1) or (await event.get_reply_message()).text.strip()
    await download_and_send_file(event, url, "YouTube")

@l313l.on(events.NewMessage(pattern=r"\.فيس(?: (.*))?", outgoing=True))
async def fb_cmd(event):
    url = event.pattern_match.group(1) or (await event.get_reply_message()).text.strip()
    await download_and_send_file(event, url, "Facebook")

@l313l.on(events.NewMessage(pattern=r"\.تويتر(?: (.*))?", outgoing=True))
async def x_cmd(event):
    url = event.pattern_match.group(1) or (await event.get_reply_message()).text.strip()
    await download_and_send_file(event, url, "Twitter")

@l313l.on(events.NewMessage(pattern=r"\.ساوند(?: (.*))?", outgoing=True))
async def sc_cmd(event):
    url = event.pattern_match.group(1) or (await event.get_reply_message()).text.strip()
    await download_and_send_file(event, url, "SoundCloud")
