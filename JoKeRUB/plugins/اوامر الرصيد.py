from JoKeRUB import l313l
from telethon import events
import os
import requests

# ملفات حفظ البيانات
ASIA_FILE = "asia_number.txt"
KASH_FILE = "kash_number.txt"
KOREK_FILE = "korek_number.txt"
TON_FILE = "ton_address.txt"
ETH_FILE = "eth_number.txt"    # رقم الاثير
USDT_FILE = "usdt_number.txt"  # رقم اليوستد

from JoKeRUB import l313l
from telethon import events
import re

# أمر عرض قائمة أوامر الرصيد مع إضافة أمر تحويل
@l313l.on(events.NewMessage(pattern=r"\.اوامر الرصيد", outgoing=True))
async def show_balance_sections(event):
    await event.reply(
        "**📦 أقسام أوامر الرصيد والمحافظ:**\n\n"
        "⥾ `.اوامر الاسيا`\n"
        "⥾ `.اوامر الماستر`\n"
        "⥾ `.اوامر الكاش`\n"
        "⥾ `.اوامر الكورك`\n"
        "⥾ `.اوامر التون`\n"
        "⥾ `.اوامر الاثير`\n"
        "⥾ `.اوامر اليوستد`\n"
        "⥾ `.اوامر تحويل`\n\n"
        "✦ أرسل أي أمر منها لعرض التعليمات الخاصة به."
    )

# أمر عرض شرح أو تعليمات أوامر التحويل
@l313l.on(events.NewMessage(pattern=r"^\.اوامر تحويل$", outgoing=True))
async def show_convert_instructions(event):
    await event.reply(
        "**📥 أوامر تحويل الرصيد 📥**\n\n"
        "⦾ `.تحويل` + رقم الهاتف + المبلغ\n"
        "مثال:\n"
        "`.تحويل 0777 10000`\n\n"
        "سيرد البوت بهذا النص القابل للنسخ:\n"
        "```\n*123*10000*077#\n```"
    )

# أمر تنفيذ تحويل الرصيد بصيغة قابلة للنسخ
@l313l.on(events.NewMessage(pattern=r'^\.تحويل\s+(\d+)\s+(\d+)$', outgoing=True))
async def convert_handler(event):
    number = event.pattern_match.group(1)
    amount = event.pattern_match.group(2)

    result = f"```\n*123*{amount}*{number}#\n```"

    await event.reply(result)


from telethon import events
import os

MASTER_FILE = "master_number.txt"

# ======== حفظ وتغيير وعرض ماستر ========
async def save_master_number(event, number):
    with open(MASTER_FILE, "w") as f:
        f.write(number)
    await event.reply(f"تم حفظ رقم الماستر: `{number}`")

@l313l.on(events.NewMessage(pattern=r"\.رقم ماستر (\d+)", outgoing=True))
async def save_master(event):
    number = event.pattern_match.group(1)
    await save_master_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.تغ ماستر (\d+)", outgoing=True))
async def change_master(event):
    number = event.pattern_match.group(1)
    await save_master_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.ماستر", outgoing=True))
async def show_master(event):
    if os.path.exists(MASTER_FILE):
        with open(MASTER_FILE, "r") as f:
            number = f.read().strip()
        await event.reply(f"رقم الماستر المحفوظ هو: `{number}`")
    else:
        await event.reply("لا يوجد رقم ماستر محفوظ بعد.")

@l313l.on(events.NewMessage(pattern=r"\.حذف ماستر", outgoing=True))
async def delete_master(event):
    if os.path.exists(MASTER_FILE):
        os.remove(MASTER_FILE)
        await event.reply("تم حذف رقم الماستر بنجاح.")
    else:
        await event.reply("لا يوجد رقم ماستر للحذف.")

# ======== امر اوامر الماستر ========
@l313l.on(events.NewMessage(pattern=r"\.اوامر الماستر", outgoing=True))
async def master_commands(event):
    commands_text = (
        "قائمة أوامر الماستر:\n"
        "• .رقم ماستر <رقم> — لحفظ رقم الماستر\n"
        "• .تغ ماستر <رقم> — لتغيير رقم الماستر\n"
        "• .ماستر — لعرض رقم الماستر المحفوظ\n"
        "• .حذف ماستر — لحذف رقم الماستر\n"
    )
    await event.reply(commands_text)


# ======== أوامر آسيا ========
@l313l.on(events.NewMessage(pattern=r"\.اوامر الاسيا", outgoing=True))
async def asia_help(event):
    await event.reply(
        "**📱 أوامر إدارة رقم اسيا:**\n\n"
        "• `.رقم اسيا <الرقم>` — لحفظ الرقم\n"
        "• `.تغ اسيا <الرقم>` — لتغييره\n"
        "• `.اسيا` — عرض الرقم المحفوظ\n"
        "• `.حذف اسيا` — حذف الرقم\n\n"
        "📌 مثال:\n"
        "`.رقم اسيا 0770xxxxxxx`"
    )

# ======== أوامر كاش ========
@l313l.on(events.NewMessage(pattern=r"\.اوامر الكاش", outgoing=True))
async def kash_help(event):
    await event.reply(
        "**💳 أوامر إدارة رقم الكاش:**\n\n"
        "• `.رقم كاش <الرقم>` — لحفظ الرقم\n"
        "• `.تغ كاش <الرقم>` — لتغييره\n"
        "• `.كاش` — عرض الرقم المحفوظ\n"
        "• `.حذف كاش` — حذف الرقم\n\n"
        "📌 مثال:\n"
        "`.رقم كاش 0780xxxxxxx`"
    )

# ======== أوامر كورك ========
@l313l.on(events.NewMessage(pattern=r"\.اوامر الكورك", outgoing=True))
async def korek_help(event):
    await event.reply(
        "**📶 أوامر إدارة رقم كورك:**\n\n"
        "• `.رقم كورك <الرقم>` — لحفظ الرقم\n"
        "• `.تغ كورك <الرقم>` — لتغييره\n"
        "• `.كورك` — عرض الرقم المحفوظ\n"
        "• `.حذف كورك` — حذف الرقم\n\n"
        "📌 مثال:\n"
        "`.رقم كورك 0750xxxxxxx`"
    )

# ======== أوامر تون ========
@l313l.on(events.NewMessage(pattern=r"\.اوامر التون", outgoing=True))
async def ton_help(event):
    await event.reply(
        "**💠 أوامر إدارة التون (TON):**\n\n"
        "• `.صرف` — عرض سعر عملة TON\n"
        "• `.ادرس تون <العنوان>` — حفظ العنوان\n"
        "• `.تغ تون <العنوان>` — تغيير العنوان\n"
        "• `.ادرسي` — عرض العنوان\n"
        "• `.مسح تون <العنوان>` — حذف العنوان\n\n"
        "📌 مثال:\n"
        "`.ادرس تون EQC6nZ...`"
    )

# ======== أوامر الاثير ========
@l313l.on(events.NewMessage(pattern=r"\.اوامر الاثير", outgoing=True))
async def eth_help(event):
    await event.reply(
        "**⛓️ أوامر إدارة رقم الاثير (ETH):**\n\n"
        "• `.رقم اثير <الرقم>` — لحفظ الرقم\n"
        "• `.تغ اثير <الرقم>` — لتغييره\n"
        "• `.اثير` — عرض الرقم المحفوظ\n"
        "• `.حذف اثير` — حذف الرقم\n\n"
        "📌 مثال:\n"
        "`.رقم اثير 0xABCDEF...`"
    )

# ======== أوامر اليوستد ========
@l313l.on(events.NewMessage(pattern=r"\.اوامر اليوستد", outgoing=True))
async def usdt_help(event):
    await event.reply(
        "**💵 أوامر إدارة اليوستد (USDT - TRC20):**\n\n"
        "• `.رقم يوستد <الرقم>` — لحفظ الرقم\n"
        "• `.تغ يوستد <الرقم>` — لتغييره\n"
        "• `.يوستد` — عرض الرقم المحفوظ\n"
        "• `.حذف يوستد` — حذف الرقم\n\n"
        "📌 مثال:\n"
        "`.رقم يوستد TXabc123...`"
    )


# ======== حفظ وتغيير وعرض آسيا ========
async def save_asia_number(event, number):
    with open(ASIA_FILE, "w") as f:
        f.write(number)
    await event.reply(f"تم حفظ رقم آسيا: `{number}`")

@l313l.on(events.NewMessage(pattern=r"\.رقم اسيا (\d+)", outgoing=True))
async def save_asia(event):
    number = event.pattern_match.group(1)
    await save_asia_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.تغ اسيا (\d+)", outgoing=True))
async def change_asia(event):
    number = event.pattern_match.group(1)
    await save_asia_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.اسيا", outgoing=True))
async def show_asia(event):
    if os.path.exists(ASIA_FILE):
        with open(ASIA_FILE, "r") as f:
            number = f.read().strip()
        await event.reply(f"رقم آسيا المحفوظ هو: `{number}`")
    else:
        await event.reply("لا يوجد رقم آسيا محفوظ بعد.")

@l313l.on(events.NewMessage(pattern=r"\.حذف اسيا", outgoing=True))
async def delete_asia(event):
    if os.path.exists(ASIA_FILE):
        os.remove(ASIA_FILE)
        await event.reply("تم حذف رقم آسيا بنجاح.")
    else:
        await event.reply("لا يوجد رقم آسيا للحذف.")

# ======== حفظ وتغيير وعرض كاش ========
async def save_kash_number(event, number):
    with open(KASH_FILE, "w") as f:
        f.write(number)
    await event.reply(f"تم حفظ رقم الكاش: `{number}`")

@l313l.on(events.NewMessage(pattern=r"\.رقم كاش (\d+)", outgoing=True))
async def save_kash(event):
    number = event.pattern_match.group(1)
    await save_kash_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.تغ كاش (\d+)", outgoing=True))
async def change_kash(event):
    number = event.pattern_match.group(1)
    await save_kash_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.كاش", outgoing=True))
async def show_kash(event):
    if os.path.exists(KASH_FILE):
        with open(KASH_FILE, "r") as f:
            number = f.read().strip()
        await event.reply(f"رقم الكاش المحفوظ هو: `{number}`")
    else:
        await event.reply("لا يوجد رقم كاش محفوظ بعد.")

@l313l.on(events.NewMessage(pattern=r"\.حذف كاش", outgoing=True))
async def delete_kash(event):
    if os.path.exists(KASH_FILE):
        os.remove(KASH_FILE)
        await event.reply("تم حذف رقم الكاش بنجاح.")
    else:
        await event.reply("لا يوجد رقم كاش للحذف.")

# ======== حفظ وتغيير وعرض كورك ========
async def save_korek_number(event, number):
    with open(KOREK_FILE, "w") as f:
        f.write(number)
    await event.reply(f"تم حفظ رقم كورك: `{number}`")

@l313l.on(events.NewMessage(pattern=r"\.رقم كورك (\d+)", outgoing=True))
async def save_korek(event):
    number = event.pattern_match.group(1)
    await save_korek_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.تغ كورك (\d+)", outgoing=True))
async def change_korek(event):
    number = event.pattern_match.group(1)
    await save_korek_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.كورك", outgoing=True))
async def show_korek(event):
    if os.path.exists(KOREK_FILE):
        with open(KOREK_FILE, "r") as f:
            number = f.read().strip()
        await event.reply(f"رقم كورك المحفوظ هو: `{number}`")
    else:
        await event.reply("لا يوجد رقم كورك محفوظ بعد.")

@l313l.on(events.NewMessage(pattern=r"\.حذف كورك", outgoing=True))
async def delete_korek(event):
    if os.path.exists(KOREK_FILE):
        os.remove(KOREK_FILE)
        await event.reply("تم حذف رقم كورك بنجاح.")
    else:
        await event.reply("لا يوجد رقم كورك للحذف.")

# ======== تون (عنوان فقط) ========
def get_ton_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd")
        response.raise_for_status()
        data = response.json()
        return data['the-open-network']['usd']
    except Exception:
        return None

@l313l.on(events.NewMessage(pattern=r"\.صرف", outgoing=True))
async def ton_command(event):
    price = get_ton_price()
    if price:
        await event.reply(f"💸 سعر عملة TON حالياً:\n`{price} $`")
    else:
        await event.reply("❌ تعذر جلب السعر حالياً.")

async def save_ton_address(event, address):
    with open(TON_FILE, "w") as f:
        f.write(address)
    await event.reply(f"تم حفظ عنوان تون: `{address}`")

@l313l.on(events.NewMessage(pattern=r"\.ادرس تون (.+)", outgoing=True))
async def save_ton(event):
    address = event.pattern_match.group(1).strip()
    await save_ton_address(event, address)

@l313l.on(events.NewMessage(pattern=r"\.تغ تون (.+)", outgoing=True))
async def change_ton(event):
    address = event.pattern_match.group(1).strip()
    await save_ton_address(event, address)

@l313l.on(events.NewMessage(pattern=r"\.مسح تون (.+)", outgoing=True))
async def delete_ton(event):
    address = event.pattern_match.group(1).strip()
    if os.path.exists(TON_FILE):
        with open(TON_FILE, "r") as f:
            saved_address = f.read().strip()
        if address == saved_address:
            os.remove(TON_FILE)
            await event.reply("تم حذف عنوان تون بنجاح.")
        else:
            await event.reply("العنوان الذي أدخلته لا يطابق العنوان المحفوظ.")
    else:
        await event.reply("لا يوجد عنوان تون محفوظ لحذفه.")

@l313l.on(events.NewMessage(pattern=r"\.ادرسي", outgoing=True))
async def show_ton(event):
    if os.path.exists(TON_FILE):
        with open(TON_FILE, "r") as f:
            address = f.read().strip()
        await event.reply(f"عنوان تون المحفوظ هو: `{address}`")
    else:
        await event.reply("لا يوجد عنوان تون محفوظ بعد.")

# ======== الاثير (رقم فقط) ========
async def save_eth_number(event, number):
    with open(ETH_FILE, "w") as f:
        f.write(number)
    await event.reply(f"تم حفظ رقم الاثير: `{number}`")

@l313l.on(events.NewMessage(pattern=r"\.رقم اثير (\d+)", outgoing=True))
async def save_eth(event):
    number = event.pattern_match.group(1)
    await save_eth_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.تغ اثير (\d+)", outgoing=True))
async def change_eth(event):
    number = event.pattern_match.group(1)
    await save_eth_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.اثير", outgoing=True))
async def show_eth(event):
    if os.path.exists(ETH_FILE):
        with open(ETH_FILE, "r") as f:
            number = f.read().strip()
        await event.reply(f"رقم الاثير المحفوظ هو: `{number}`")
    else:
        await event.reply("لا يوجد رقم اثير محفوظ بعد.")

@l313l.on(events.NewMessage(pattern=r"\.حذف اثير", outgoing=True))
async def delete_eth(event):
    if os.path.exists(ETH_FILE):
        os.remove(ETH_FILE)
        await event.reply("تم حذف رقم اثير بنجاح.")
    else:
        await event.reply("لا يوجد رقم اثير للحذف.")

# ======== اليوستد (رقم فقط) ========
async def save_usdt_number(event, number):
    with open(USDT_FILE, "w") as f:
        f.write(number)
    await event.reply(f"تم حفظ رقم اليوستد: `{number}`")

@l313l.on(events.NewMessage(pattern=r"\.رقم يوستد (\d+)", outgoing=True))
async def save_usdt(event):
    number = event.pattern_match.group(1)
    await save_usdt_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.تغ يوستد (\d+)", outgoing=True))
async def change_usdt(event):
    number = event.pattern_match.group(1)
    await save_usdt_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.يوستد", outgoing=True))
async def show_usdt(event):
    if os.path.exists(USDT_FILE):
        with open(USDT_FILE, "r") as f:
            number = f.read().strip()
        await event.reply(f"رقم اليوستد المحفوظ هو: `{number}`")
    else:
        await event.reply("لا يوجد رقم يوستد محفوظ بعد.")

@l313l.on(events.NewMessage(pattern=r"\.حذف يوستد", outgoing=True))
async def delete_usdt(event):
    if os.path.exists(USDT_FILE):
        os.remove(USDT_FILE)
        await event.reply("تم حذف رقم يوستد بنجاح.")
    else:
        await event.reply("لا يوجد رقم يوستد للحذف.")
from JoKeRUB import l313l
from telethon import events
import re

@l313l.on(events.NewMessage(pattern=r'^\.تحويل\s+(\d+)\s+(\d+)$', outgoing=True))
async def convert_handler(event):
    number = event.pattern_match.group(1)
    amount = event.pattern_match.group(2)

    # النص داخل كود ليظهر بشكل قابل للنسخ
    result = f"```\n*123*{amount}*{number}#\n```"

    await event.reply(result)

