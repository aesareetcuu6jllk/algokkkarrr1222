from JoKeRUB import l313l
from telethon import events
import subprocess
import os
import tempfile
import json
import re
import asyncio

URL_REGEX = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

async def download_and_send_file(event, url, platform):
    chat = await event.get_chat()
    try:
        await event.reply(f"جاري التحميل من {platform}، يرجى الانتظار قد يستغرق الأمر بعض الوقت...")

        with tempfile.TemporaryDirectory() as tmpdir:
            output_template = os.path.join(tmpdir, '%(title)s.%(ext)s')

            try:
                info_command = [
                    'yt-dlp',
                    '--no-warnings',
                    '--flat-playlist',
                    '--dump-json',
                    url
                ]
                info_process = subprocess.run(info_command, capture_output=True, text=True, check=True)
                video_info = json.loads(info_process.stdout)

                if video_info.get('_type') == 'playlist':
                    await event.reply("عذراً، لا أدعم تحميل قوائم التشغيل. يرجى إرسال رابط فيديو مفرد.")
                    return

                estimated_filesize = video_info.get('filesize') or video_info.get('filesize_approx')
                if estimated_filesize and estimated_filesize > 2 * 1024 * 1024 * 1024:
                    await event.reply("❌ الملف كبير جداً (أكثر من 2 غيغابايت) ولا يمكن إرساله عبر تيليجرام.")
                    return

                format_selector = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'
                if video_info.get('is_live'):
                    format_selector = 'best[ext=mp4]'
                elif video_info.get('ext') == 'mp3' or video_info.get('acodec') != 'none':
                    format_selector = 'bestaudio/best'

            except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
                await event.reply("❌ لم أستطع الحصول على معلومات حول الرابط. تأكد من صحته.")
                return

            download_command = [
                'yt-dlp',
                '--no-warnings',
                '-f', format_selector,
                '--output', output_template,
                url
            ]

            process = subprocess.run(download_command, cwd=tmpdir, capture_output=True, text=True, check=True)

            downloaded_files = [os.path.join(tmpdir, f) for f in os.listdir(tmpdir) if f.startswith(video_info.get('title', ''))]
            if not downloaded_files:
                await event.reply("❌ لم يتم العثور على أي ملفات بعد التحميل.")
                return

            downloaded_file = next((f for f in downloaded_files if f.endswith(('.mp4', '.mkv', '.webm'))), None)
            if not downloaded_file:
                downloaded_file = next((f for f in downloaded_files if f.endswith(('.mp3', '.m4a', '.ogg'))), None)
            if not downloaded_file:
                downloaded_file = downloaded_files[0]

            file_size = os.path.getsize(downloaded_file)
            if file_size > 2 * 1024 * 1024 * 1024:
                await event.reply("❌ الملف كبير جداً (أكثر من 2 غيغابايت) ولا يمكن إرساله عبر تيليجرام.")
                return

            await event.reply("⬆️ جاري رفع الملف إلى تيليجرام...")

            try:
                file_extension = os.path.splitext(downloaded_file)[1].lower()
                title = video_info.get('title', 'بدون عنوان')

                if file_extension in ['.mp4', '.mkv', '.webm']:
                    await l313l.send_file('me', downloaded_file, caption=f"🎬 {title}\nتم التحميل من {platform}", video_note=False)
                elif file_extension in ['.mp3', '.m4a', '.ogg', '.wav']:
                    await l313l.send_file('me', downloaded_file, caption=f"🎧 {title}\nتم التحميل من {platform}")
                else:
                    await l313l.send_file('me', downloaded_file, caption=f"📁 {title}\nتم التحميل من {platform}")
                await event.reply("✅ تم إرسال الملف بنجاح!")
            except Exception as e:
                await event.reply(f"❌ فشل إرسال الملف: {e}")

    except subprocess.CalledProcessError as e:
        await event.reply(f"❌ فشل التحميل من {platform}. الخطأ: {e.stderr}")
    except Exception as e:
        await event.reply(f"❌ حدث خطأ: {e}")


@l313l.on(events.NewMessage(pattern=r'^/اوامر التحميل$', outgoing=True))
async def send_welcome(event):
    msg = (
        "🎉 **أهلاً بك في بوت التحميل** \n"
        "اكتب `.تيكتوك` أو `.انستا` أو `.يوتيوب` مع الرابط أو بالرد على رابط.")
    await event.reply(msg)


@l313l.on(events.NewMessage(pattern=r"\.تيكتوك(?: (.*))?", outgoing=True))
async def tiktok_cmd(event):
    url = event.pattern_match.group(1) or (await event.get_reply_message()).text.strip()
    await download_and_send_file(event, url, "TikTok")

@l313l.on(events.NewMessage(pattern=r"\.انستا(?: (.*))?", outgoing=True))
async def insta_cmd(event):
    url = event.pattern_match.group(1) or (await event.get_reply_message()).text.strip()
    await download_and_send_file(event, url, "Instagram")

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

