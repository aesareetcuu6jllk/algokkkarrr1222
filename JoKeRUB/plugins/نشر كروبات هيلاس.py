from JoKeRUB import l313l
from telethon import events
import asyncio

# حالة التكرار
repeat_active = False

# عرض قائمة أوامر النشر
@l313l.on(events.NewMessage(from_users='me', pattern=r'^\.اوامر النشر$'))
async def show_publish_commands(event):
    await event.delete()
    message = (
        "**📢 أوامر النشر التلقائي:**\n\n"
        "🔹 **الأوامر المحددة (تحتاج الرد على رسالة):**\n"
        "▪️ `.نشر_كروبات 60`\n"
        "↳ نشر الرسالة التي ترد عليها في كل الكروبات كل 60 ثانية.\n\n"
        "▪️ `.نشر_عدد 60 5`\n"
        "↳ نشر الرسالة التي ترد عليها في أول 5 كروبات كل 60 ثانية.\n\n"
        "🔹 **الأوامر غير المحددة (تنفذ مباشرة):**\n"
        "▪️ `.ايقاف_نشر_كروبات`\n"
        "↳ إيقاف النشر المستمر في كل الكروبات.\n\n"
        "▪️ `.ايقاف_نشر_عدد`\n"
        "↳ إيقاف النشر المحدود.\n\n"
        "🔹 **أمر التكرار (يعمل فقط في المجموعات):**\n"
        "▪️ `.مكرر 300 10000`\n"
        "↳ تكرار الرسالة التي ترد عليها 10000 مرة، كل 300 ثانية بين كل تكرار.\n\n"
        "▪️ `.ايقاف التكرار`\n"
        "🔹 **تعليمات هامة:**\n"
        "• قم بالرد على الرسالة التي تريد نشرها قبل استخدام أوامر النشر المحددة.\n"
        "• الأوامر الخاصة بالإيقاف تعمل فورًا بدون الحاجة لرد.\n"
        "• تأكد من أن البوت يعمل وله صلاحيات النشر في الكروبات المستهدفة.\n"
    )
    await event.respond(message)

# أمر التكرار .مكرر
@l313l.on(events.NewMessage(from_users='me', pattern=r'^\.مكرر (\d+)\s+(\d+)$'))
async def repeated_sender(event):
    await event.delete()
    delay, count = map(int, event.pattern_match.groups())

    message = await event.get_reply_message()
    if not message:
        return await event.respond("❌ يجب الرد على الرسالة التي تريد تكرارها!")

    await event.respond(f"✅ سيتم تكرار الرسالة {count} مرة كل {delay} ثانية.\n🛑 للإيقاف، أرسل `.ايقاف_مكرر`.")

    global repeat_active
    repeat_active = True
    for i in range(count):
        if not repeat_active:
            break
        try:
            if message.text:
                await event.respond(message.text)
            elif message.media:
                await l313l.send_file(event.chat_id, message.media, caption=message.text)
            await asyncio.sleep(delay)
        except Exception as e:
            print(f"❌ خطأ أثناء التكرار: {e}")

# أمر إيقاف التكرار

