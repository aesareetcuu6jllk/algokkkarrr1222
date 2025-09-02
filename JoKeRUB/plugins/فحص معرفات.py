import re
import asyncio
from telethon import events
from JoKeRUB import l313l

CHECK_GROUP_LINK = "https://t.me/sekknft"

pending_checks = {}

@l313l.on(events.NewMessage(pattern=r"^.معرفاته(?:\s+(.*))?"))
async def sandal_cmd(event):
    me = await l313l.get_me()
    if event.sender_id != me.id:
        return

    input_text = event.pattern_match.group(1)
    if not input_text:
        reply = await event.get_reply_message()
        if reply:
            input_text = reply.text or ""
        else:
            return await event.reply("❌ يرجى كتابة المعرف أو الرد على رسالة.")

    usernames = re.findall(r"@[\w\d_]{5,32}", input_text)
    if not usernames:
        return await event.reply("❌ لم يتم العثور على أي معرف بالرسالة.")

    for user in usernames:
        try:
            sent_msg = await l313l.send_message(CHECK_GROUP_LINK, f"فحص {user}")
            pending_checks[sent_msg.id] = (event, user)
        except Exception as e:
            await event.reply(f"❌ فشل إرسال الفحص للمعرف {user}:\n{e}")


@l313l.on(events.NewMessage(chats=CHECK_GROUP_LINK))
async def on_group_reply(event):
    if not event.is_reply:
        return

    replied_msg_id = event.reply_to_msg_id
    if replied_msg_id not in pending_checks:
        return

    user_event, username = pending_checks.pop(replied_msg_id)

    # ما نرسل رسالة "يتم الجلب" — نتعامل مباشرة
    final_text = event.text or ""

    # نضغط زر عرض كل اليوزرات تلقائياً (إذا موجود)
    try:
        if getattr(event, "buttons", None):
            await event.click(text="عرض كل اليوزرات")

            msg_id = event.id
            bot_id = event.sender_id

            try:
                edited = await l313l.wait_for(
                    events.MessageEdited(chats=CHECK_GROUP_LINK, ids=msg_id),
                    timeout=8
                )
                final_text = edited.text or final_text
            except asyncio.TimeoutError:
                try:
                    new_msg = await l313l.wait_for(
                        events.NewMessage(chats=CHECK_GROUP_LINK, from_users=bot_id),
                        timeout=5
                    )
                    final_text = new_msg.text or final_text
                except asyncio.TimeoutError:
                    pass
    except Exception:
        pass

    # === استخراج البيانات وصياغتها بالقالب المطلوب ===

    # رصيد TON (أرقام مع فاصلة عشرية واستخدام , للفواصل)
    ton_m = re.search(r'Balance\s*[:\-]?\s*([\d,]+(?:\.\d+)?)\s*TON', final_text, re.IGNORECASE)
    ton_val = ton_m.group(1) if ton_m else "غير متوفر"

    # قيمة بالدولار (نلتقط اللي بعد ≈ أو أي $)
    usd_m = re.search(r'≈\s*\$?\s*([\d,]+(?:\.\d+)?)', final_text) or \
            re.search(r'\$\s*([\d,]+(?:\.\d+)?)', final_text)
    usd_val = usd_m.group(1) if usd_m else "غير متوفر"

    # اليوزرات (نلتقط الكل ثم نزيل المكرر مع الحفاظ على الترتيب)
    found_users = re.findall(r'@[\w\d_]{3,32}', final_text)
    seen = set()
    users_unique = []
    for u in found_users:
        if u not in seen:
            users_unique.append(u)
            seen.add(u)

    users_count = len(users_unique)
    users_line = " ".join(users_unique) if users_unique else "لا يوجد"

    # الرسالة بالصياغة التي طلبتها بالضبط
    out = (
        "- معلومات عن المحفظة:-\n\n"
        f"- Balance : {ton_val} TON ≈ ${usd_val}\n\n"
        f"- Users Count ({users_count}) : {users_line}"
    )

    # نرسلها في نفس مكان ما كتبت الأمر وعلى شكل رد
    await l313l.send_message(user_event.chat_id, out, reply_to=user_event.id)
