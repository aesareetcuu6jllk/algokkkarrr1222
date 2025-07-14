from JoKeRUB import l313l
from telethon import events
import requests
import io
import random
import time
import re

# أنماط الذكاء
STYLE_MODIFIERS = {
    "سينمائي": "cinematic, detailed, masterpiece, high quality, 8k",
    "أنمي": "anime style, vibrant colors, dynamic pose, studio quality",
    "فانتاسي": "fantasy art, epic, magical, intricate details, atmospheric lighting",
    "مستقبلي": "futuristic, cyberpunk, neon lights, high tech, detailed machinery",
    "كلاسيكي": "vintage aesthetic, sepia tone, retro style, nostalgic, old photo",
    "كرتون": "cartoon style, whimsical, expressive, bright, comic art",
    "مائي": "watercolor painting, soft colors, delicate brushstrokes, artistic",
    "سايبربنك": "cyberpunk, dystopian, neon, high contrast, futuristic city",
    "تجريدي": "abstract art, conceptual, non-representational, unique composition",
    "واقعي": "photorealistic, hyperdetailed, sharp focus, natural lighting",
}

# تقييد الطلبات
user_last_request = {}
RATE_LIMIT_SECONDS = 5

# دالة توليد الصورة
async def generate_image(event, prompt, count=1):
    user_id = event.sender_id

    if user_id in user_last_request:
        last_time = user_last_request[user_id]
        if time.time() - last_time < RATE_LIMIT_SECONDS:
            await event.reply("⏳ يرجى الانتظار قليلاً قبل طلب صورة أخرى.")
            return

    user_last_request[user_id] = time.time()
    await event.reply("🔄 جارٍ توليد الصورة...")

    success = 0
    fail = 0
    files_to_send = []

    for _ in range(min(count, 5)):
        try:
            response = requests.post(
                "http://185.158.132.66:2010/api/tnt/tnt-black-image",
                json={"User-Prompt": prompt},
                timeout=45
            )

            if response.status_code != 200:
                fail += 1
                continue

            data = response.json()
            images = data.get("url-image", [])

            if not images:
                fail += 1
                continue

            image_url = random.choice(images)
            image_data = requests.get(image_url, timeout=30).content
            image_io = io.BytesIO(image_data)
            image_io.name = f"generated_{success+1}.jpg"
            files_to_send.append(image_io)
            success += 1

        except Exception as e:
            fail += 1
            continue

    if success > 0:
        try:
            await l313l.send_file(event.chat_id, files=files_to_send)
        except Exception as e:
            await event.reply(f"❌ خطأ أثناء إرسال الصور:\n{e}")

    if count > 1:
        await event.reply(f"✅ تم توليد {success} صورة، وفشل {fail}.")


# أوامر الذكاء الاصطناعي (خاص بالمالك فقط)
@l313l.on(events.NewMessage(pattern=r'^\.اوامر الذكاء$', outgoing=True))
async def image_ai_commands(event):
    me = await l313l.get_me()
    if event.sender_id != me.id:
        return

    await event.edit(
        "**🤖 قائمة أوامر ذكاء الصور:**\n"
        "★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n"
        "• `.صنع صوره +الوصف` ⦙ توليد صورة.\n"
        "  ✦ مثال: `.صنع صوره +قطة تلبس نظارات`\n"
        "• لتوليد عدة صور:\n"
        "  ✦ `.صنع صوره +روبوت يطير #3`\n"
        "• لإضافة ستايل:\n"
        "  ✦ `.صنع صوره +بنت تقرأ كتاب +كرتون`\n"
        "🖌️ الأنماط:\n"
        "`كرتون`, `واقعي`, `سينمائي`, `فانتاسي`, `أنمي`, `مستقبلي`, `سايبربنك`, `كلاسيكي`, `مائي`, `تجريدي`\n"
        "⌛ مهلة 5 ثوانٍ بين كل طلب."
    )


# أمر صنع صوره
@l313l.on(events.NewMessage(pattern=r"\.صنع صوره \+(.+)", outgoing=True))
async def photo_generator(event):
    me = await l313l.get_me()
    if event.sender_id != me.id:
        return

    input_text = event.pattern_match.group(1).strip()

    # استخراج العدد إن وجد
    match = re.match(r"(.*?)\s*#(\d+)$", input_text)
    if match:
        prompt = match.group(1).strip()
        count = int(match.group(2))
    else:
        prompt = input_text
        count = 1

    # فحص النمط داخل الوصف
    for style_arabic, style_prompt in STYLE_MODIFIERS.items():
        if f"+{style_arabic}" in prompt:
            prompt = prompt.replace(f"+{style_arabic}", "").strip()
            prompt += f", {style_prompt}"
            break

    if not prompt:
        await event.reply("❌ يرجى كتابة وصف بعد +")
        return

    await generate_image(event, prompt, count)
