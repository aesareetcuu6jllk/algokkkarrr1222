from JoKeRUB import l313l
from telethon import events
import os

ASIA_FILE = "asia_number.txt"

async def save_number(event, number):
    with open(ASIA_FILE, "w") as f:
        f.write(number)
    await event.reply(f"تم حفظ رقم اسيا: {number}")

@l313l.on(events.NewMessage(pattern=r"\.رقم اسيا (\d+)", outgoing=True))
async def save_asia_number(event):
    number = event.pattern_match.group(1)
    await save_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.تغ اسيا (\d+)", outgoing=True))
async def change_asia_number(event):
    number = event.pattern_match.group(1)
    await save_number(event, number)

@l313l.on(events.NewMessage(pattern=r"\.اسيا", outgoing=True))
async def show_asia_number(event):
    if os.path.exists(ASIA_FILE):
        with open(ASIA_FILE, "r") as f:
            number = f.read().strip()
        await event.reply(f"رقم اسيا المحفوظ هو: {number}")
    else:
        await event.reply("لا يوجد رقم اسيا محفوظ بعد.")

@l313l.on(events.NewMessage(pattern=r"\.حذف اسيا", outgoing=True))
async def delete_asia_number(event):
    if os.path.exists(ASIA_FILE):
        os.remove(ASIA_FILE)
        await event.reply("تم حذف رقم اسيا بنجاح.")
    else:
        await event.reply("لا يوجد رقم لحذفه.")

# أمر أوامر الأرقام (تعليمات)
@l313l.on(events.NewMessage(pattern=r"\.اوامر الارقام", outgoing=True))
async def numbers_commands(event):
    text = (
        "📱 **أوامر إدارة رقم اسيا:**\n\n"
        "1. `.رقم اسيا <الرقم>`  ➡️ لحفظ رقم اسيا جديد.\n"
        "2. `.تغ اسيا <الرقم>`  ➡️ لتغيير الرقم المحفوظ.\n"
        "3. `.اسيا`  ➡️ لعرض الرقم المحفوظ.\n"
        "4. `.حذف اسيا`  ➡️ لحذف الرقم المحفوظ.\n\n"
        "مثال:\n"
        "`.رقم اسيا 07761536735`\n"
        "`.تغ اسيا 07760000000`\n"
        "`.اسيا`\n"
        "`.حذف اسيا`\n"
    )
    await event.reply(text)
