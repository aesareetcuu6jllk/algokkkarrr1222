from JoKeRUB import l313l
from telethon import events
import requests
import base64
import random

# API مجاني من HuggingFace لتوليد الصور
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/gsdf/Counterfeit-V2.5"

# ردود افتراضية عند حدوث خطأ
UNKNOWN_RESPONSES = [
    "❌ لم يتم إنشاء الصورة، حاول مرة أخرى.",
    "❌ حدث خطأ في الاتصال بالـ API."
]

# دالة توليد الصورة من HuggingFace
async def generate_image(prompt: str) -> str:
    try:
        payload = {"inputs": prompt}
        response = requests.post(HUGGINGFACE_API_URL, json=payload)
        if response.status_code == 200:
            # API يرجع صورة مباشرة في شكل base64
            image_bytes = response.content
            # حفظ الصورة مؤقتاً
            filename = f"{prompt[:20].replace(' ','_')}.png"
            with open(filename, "wb") as f:
                f.write(image_bytes)
            return filename  # نرسل اسم الملف كي يتم إرساله في تيليجرام
        else:
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
    
    image_file = await generate_image(prompt)
    
    if image_file.endswith(".png"):
        # إرسال الصورة في تيليجرام
        await event.reply(file=image_file)
    else:
        # إرسال رسالة الخطأ
        await event.reply(image_file)
