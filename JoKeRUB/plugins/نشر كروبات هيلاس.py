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
         "▪️ `.فحص النشر`\n"
         "▪️ `.حالتي`\n"
        "🔹 **تعليمات هامة:**\n"
        "• قم بالرد على الرسالة التي تريد نشرها قبل استخدام أوامر النشر المحددة.\n"
        "• الأوامر الخاصة بالإيقاف تعمل فورًا بدون الحاجة لرد.\n"
        "• تأكد من أن البوت يعمل وله صلاحيات النشر في الكروبات المستهدفة.\n"
    )
    await event.respond(message)


@client.on(events.NewMessage(pattern=r"\.حالتي(?: |$)(.*)"))
async def _(event):
    await event.edit("**- يتم التأكد من حالتك إذا كنت محظورًا أو لا...**")
    
    async with event.client.conversation("@SpamBot") as conv:
        try:
            await conv.send_message("/start")
            response = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("**أولًا، قم بإلغاء حظر @SpamBot ثم حاول مجددًا.**")
            return

    await event.edit(f"- {response.message}\n@HELLASUserBot")

@l313l.on(events.NewMessage(from_users='me', pattern=r'^\.فحص النشر$'))
async def check_broadcast_status(event):
    await event.delete()

    status_all = "✅ مفعل" if final_krobats_active else "⛔️ متوقف"
    status_limited = "✅ مفعل" if final_limited_broadcast else "⛔️ متوقف"
    status_repeat = "✅ مفعل" if repeat_active else "⛔️ متوقف"

    message = (
        "**📊 حالة أوامر النشر الحالية:**\n\n"
        f"🔄 النشر في كل الكروبات: {status_all}\n"
        f"🔢 النشر المحدود (عدد معين): {status_limited}\n"
        f"♻️ التكرار المتواصل: {status_repeat}\n"
    )

    await event.respond(message)


