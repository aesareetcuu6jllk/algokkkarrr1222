import os
import requests
from JoKeRUB import l313l
from telethon import events

# تأكد من وجود مجلد التنزيل
os.makedirs("downloads", exist_ok=True)

@l313l.on(events.NewMessage(pattern=r"^.تحميل يوت (.+)"))
async def clipto_download(event):
    query = event.pattern_match.group(1).strip()
    if not query:
        await event.reply("❌ اكتب الرابط بعد الأمر مثل:\n.تحميل يوت https://youtube.com/watch?v=...")
        return

    api_url = f"http://145.223.80.56:5001/get?q={requests.utils.quote(query)}"

    try:
        response = requests.get(api_url, timeout=10)
        data = response.json()
    except Exception:
        await event.reply("⚠️ حدث خطأ أثناء الاتصال بـ API.")
        return

    if 'رابط الصوت' in data:
        audio_url = data['رابط الصوت']
        temp_file = f"downloads/{os.urandom(4).hex()}.mp3"

        try:
            audio_data = requests.get(audio_url).content
            with open(temp_file, "wb") as f:
                f.write(audio_data)

            await event.reply(
                file=temp_file,
                caption="*- Uploader : @laiecbot*",
                parse_mode="markdown"
            )
            os.remove(temp_file)

        except Exception:
            await event.reply("⚠️ حدث خطأ أثناء تحميل أو إرسال الملف.")
    else:
        await event.reply("*- لم يتم العثور على نتيجة .*", parse_mode="markdown")
