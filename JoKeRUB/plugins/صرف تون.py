from JoKeRUB import l313l
from telethon import events
import requests

OWNER_ID = None  # يتم تعيينه تلقائيًا أول مرة

# دالة جلب سعر TON
def get_ton_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd")
        response.raise_for_status()
        data = response.json()
        return data['the-open-network']['usd']
    except Exception:
        return None

# أمر .صرف — فقط لصاحب أول مرة
@l313l.on(events.NewMessage(pattern=r"\.صرف"))
async def ton_command(event):
    global OWNER_ID
    sender = await event.get_sender()
    
    # أول مرة يتم تعيين المالك
    if OWNER_ID is None:
        OWNER_ID = sender.id
        await event.reply("✅ تم تعيينك كمالك لهذا الأمر.")
    
    # إذا شخص ثاني حاول يكتب الأمر
    if sender.id != OWNER_ID:
        return  # تجاهل
    
    # الرد بالسعر
    price = get_ton_price()
    if price:
        await event.reply(f"💸 سعر عملة TON حالياً:\n`{price} $`")
    else:
        await event.reply("❌ تعذر جلب السعر حالياً.")
