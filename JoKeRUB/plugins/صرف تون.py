from JoKeRUB import l313l
from telethon import events
import requests
import os

TON_FILE = "ton_address.txt"

# دالة جلب سعر TON
def get_ton_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd")
        response.raise_for_status()
        data = response.json()
        return data['the-open-network']['usd']
    except Exception:
        return None

# أمر .صرف — يشتغل فقط لأوامرك (outgoing=True)
@l313l.on(events.NewMessage(pattern=r"\.صرف", outgoing=True))
async def ton_command(event):
    price = get_ton_price()
    if price:
        await event.reply(f"💸 سعر عملة TON حالياً:\n`{price} $`")
    else:
        await event.reply("❌ تعذر جلب السعر حالياً.")

# حفظ عنوان تون
async def save_address(event, address):
    with open(TON_FILE, "w") as f:
        f.write(address)
    await event.reply(f"تم حفظ عنوان تون: {address}")

@l313l.on(events.NewMessage(pattern=r"\.ادرس تون (.+)", outgoing=True))
async def save_ton_address(event):
    address = event.pattern_match.group(1).strip()
    await save_address(event, address)

@l313l.on(events.NewMessage(pattern=r"\.تغ تون (.+)", outgoing=True))
async def change_ton_address(event):
    address = event.pattern_match.group(1).strip()
    await save_address(event, address)

@l313l.on(events.NewMessage(pattern=r"\.مسح تون (.+)", outgoing=True))
async def delete_ton_address(event):
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
async def show_ton_address(event):
    if os.path.exists(TON_FILE):
        with open(TON_FILE, "r") as f:
            address = f.read().strip()
        await event.reply(f"عنوان تون المحفوظ هو: {address}")
    else:
        await event.reply("لا يوجد عنوان تون محفوظ بعد.")
