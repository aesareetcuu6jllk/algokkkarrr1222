from JoKeRUB import l313l
from telethon.tl.functions.users import GetFullUserRequest
import re

# وظيفة استخراج اليوزر من نص الرسالة
def extract_username(text):
    matches = re.findall(r'@(\w+)', text)
    if matches:
        return matches[0]  # يرجع أول يوزر موجود بالرسالة
    return None

@l313l.on(events.NewMessage(pattern=r'^\.يوزر$', func=lambda e: e.is_reply))
async def _(event):
    reply = await event.get_reply_message()
    if not reply:
        await event.reply("❌ لازم ترد على رسالة فيها يوزر.")
        return

    username = extract_username(reply.text)
    if not username:
        await event.reply("❌ ما لكيت أي يوزر بالرسالة.")
        return

    try:
        user = await event.client.get_entity(username)
        full = await event.client(GetFullUserRequest(user.id))
        if hasattr(full.full_user, 'premium_usernames') and full.full_user.premium_usernames:
            await event.reply(f"✅ اليوزر @{username} هو 'منصة / NFT' (مباع عبر تيليجرام).")
        else:
            await event.reply(f"👤 اليوزر @{username} ملكية عادية (شخصية).")
    except Exception as e:
        await event.reply(f"⚠️ خطأ أثناء الفحص: {e}")
