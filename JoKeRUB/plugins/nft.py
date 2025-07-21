from JoKeRUB import l313l
from telethon import events
import asyncio

BOT_USERNAME = "hdysendbot"  # ← هذا هو بوت الفحص الحقيقي

@l313l.client.on(events.NewMessage(pattern=r'^\.يوزر\s+@?(\w+)$'))
async def _(event):
    username = event.pattern_match.group(1)
    await event.reply("🔍 جارٍ فحص المعرف، الرجاء الانتظار ...")

    try:
        bot = await l313l.client.get_entity(BOT_USERNAME)
        async with l313l.client.conversation(bot, timeout=20) as conv:
            await conv.send_message(f"/check @{username}")
            await conv.get_response()  # أول رد ← نتجاهله
            response2 = await conv.get_response()  # ثاني رد ← نستخدمه

            await event.reply(response2.text)

    except asyncio.TimeoutError:
        await event.reply("⛔ تأخر الرد من البوت.")
    except Exception as e:
        await event.reply(f"❌ حدث خطأ: {e}")

