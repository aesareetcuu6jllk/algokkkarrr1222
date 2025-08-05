# 📦 الاستيرادات اللازمة من السورس
import asyncio
import io
import re
import requests
import time

from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest

from JoKeRUB import bot
from JoKeRUB.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from JoKeRUB.sql_helper.botusers_sql import add_me_in_db, his_userid
from JoKeRUB.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)
from l313l.razan.resources.assistant import *  # إذا تستخدم دوال إضافية

# ✅ أمر .يوزر
@bot.on(events.NewMessage(pattern=r"\.يوزر(?:\s+@?(\w+))?"))
async def check_username(event):
    username = event.pattern_match.group(1)

    if not username:
        return await event.reply("❌ يرجى كتابة المعرف بعد الأمر.\nمثال: `.يوزر @MMMFi`")

    await event.reply(f"🔍 يتم الآن فحص المعرف: @{username} ...")

    start = time.time()
    url = f"https://fragment.com/username/{username}"
    response = requests.get(url)
    end = time.time()

    if response.status_code == 200:
        html = response.text
        is_taken = '<span class="tm-section-header-status tm-status-taken">Taken</span>' in html
        status = "❌ ليس NFT (تم حجزه)" if is_taken else "✅ متاح / NFT"

        usd = re.search(r'<span class="js-bid_usd_value">([^<]+)</span>', html)
        ton = re.search(r'<div class="table-cell-value tm-value icon-before icon-ton">\s*([\d,]+)\s*</div>', html)

        usd_value = usd.group(1) if usd else "غير معروف"
        ton_value = ton.group(1) if ton else "غير معروف"
        elapsed = round(end - start, 2)

        result = (
            f"📊 **نتيجة الفحص:**\n\n"
            f"- المعرف: `@{username}`\n"
            f"- الحالة: **{status}**\n"
            f"- Ton: `{ton_value}`\n"
            f"- USD: `{usd_value}$`\n"
            f"- الزمن: `{elapsed} ثانية`\n\n"
            f"[رابط العرض في Fragment 🌐]({url})"
        )

        await event.respond(result, link_preview=False)
    else:
        await event.respond("⚠️ حدث خطأ أثناء الاتصال بموقع Fragment.")

