from JoKeRUB import l313l
from telethon import events
import requests
import json
import random

# ردود افتراضية في حال حدوث خطأ
UNKNOWN_RESPONSES = [
    "❌ لم يتم إنشاء الصورة، حاول مرة أخرى.",
    "❌ حدث خطأ في الاتصال بالـ API."
]

# دالة توليد الصورة من PhotoRoom
async def generate_image(prompt: str) -> str:
    try:
        headers = {
            'Host': 'serverless-api.photoroom.com',
            'Accept': 'text/event-stream',
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'okhttp/4.12.0',
            'X-App-Version': '2025.12.02 (1799)',
            'Pr-Platform': 'and',
            'Pr-App-Version': '2025.12.02',
            'Pr-User-Pro-Status': 'pro',
            'Pr-User-Bcp-Language': 'en-US',
            'Pr-Telemetry-Enabled': 'true',
        }

        json_data = {
            'userPrompt': prompt,
            'appId': 'expert',
            'styleId': 'diversity',
            'sizeId': 'SQUARE_HD',
            'numberOfImages': 1,
        }

        response = requests.post(
            'https://serverless-api.photoroom.com/v2/ai-tools/generate-images',
            headers=headers,
            json=json_data,
            verify=False,
        ).text

        lines = response.splitlines()
        for line in lines:
            if line.startswith("data: ") and "aiImageResult" in line:
                json_line = json.loads(line[6:])
                image_url = json_line.get("imageUrl")
                if image_url:
                    return image_url
        return random.choice(UNKNOWN_RESPONSES)

    except requests.exceptions.RequestException:
        return random.choice(UNKNOWN_RESPONSES)


# حدث يستمع للأمر ".توليد صوره + الوصف"
@l313l.on(events.NewMessage(pattern=r"^\.توليد صوره(?: (.+))?"))
async def image_handler(event):
    # استخراج الوصف بعد الأمر
    prompt = event.pattern_match.group(1)
    
    # إذا لم يكتب المستخدم وصف، استخدم l313l() لتوليد نص عشوائي
    if not prompt:
        prompt = l313l()

    await event.reply(f"🎨 جارٍ توليد الصورة للوصف: '{prompt}' ...")
    
    image_url = await generate_image(prompt)
    await event.reply(image_url)
