import os
from contextlib import suppress
from telethon import TelegramClient
from telethon.tl.types import User, UserFull
from telethon.tl.functions.users import GetFullUserRequest
from telethon.events import NewMessage
from JoKeRUB import l313l  # استيراد الديكور من JoKeRUB

@l313l("ستوري")
async def stories(event: NewMessage.Event):
    replied = await event.get_reply_message()
    await event.eor("**⌔∮ جار تنزيل الستوري يرجى الانتظار**")

    try:
        username = event.text.split(maxsplit=1)[1]
    except IndexError:
        if replied and isinstance(replied.sender, User):
            username = replied.sender_id
        else:
            return await event.eor("**⌔∮ يجب عليك وضع يوزر المستخدم لتنزيل الستوري الخاص به**")

    with suppress(ValueError):
        username = int(username)

    try:
        full_user: UserFull = (
            await event.client(GetFullUserRequest(id=username))
        ).full_user
    except Exception as er:
        return await event.eor(f"**❃ خطأ : {er}**")

    stories = full_user.stories
    if not (stories and stories.stories):
        return await event.eor("**⌔∮ لم يتم العثور على ستوري خاص بالمستخدم**")

    for story in stories.stories:
        file = await event.client.download_media(story.media)
        await event.reply(
            story.caption if story.caption else "",
            file=file
        )
        os.remove(file)

    await event.eor("**⌔∮ تم بنجاح تحميل الستوري ✅**", time=5)
