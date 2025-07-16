from JoKeRUB import l313l
import requests

@l313l.on_message(l313l.filters.command("الانشاء", prefixes=".") & l313l.filters.me)
async def creation_handler(client, message):
    try:
        # إذا كان رد على شخص
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            user_id = message.from_user.id

        url = f"http://145.223.80.56:5016/date?id={user_id}"
        response = requests.get(url)

        if response.status_code == 200:
            await message.reply(f"تاريخ الانشاء:\n{response.text}")
        else:
            await message.reply("❌ لم أستطع جلب تاريخ الإنشاء.")
    except Exception as e:
        await message.reply(f"❌ حدث خطأ:\n{str(e)}")
