import asyncio
import re
from telethon.errors.rpcerrorlist import YouBlockedUserError

from JoKeRUB import l313l
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import get_user_from_event
from ..helpers.utils import _format

plugin_category = "utils"

@l313l.ar_cmd(
    pattern=r"يوزر(?: |$)(.*)",
    command=("يوزر", plugin_category),
    info={
        "header": "فحص سجل اسم المستخدم من @SangMataInfo_bot",
        "usage": ["{tr}يوزر @username أو بالرد على رسالة"],
        "examples": "{tr}يوزر @example",
    },
)
async def _(event):
    input_text = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    username = None
    user = None

    # من الرد
    if reply and reply.sender_id:
        user, _ = await get_user_from_event(event)
        if user.username:
            username = f"@{user.username}"

    # من النص
    if not username and input_text:
        match = re.search(r"@[\w\d_]{5,}", input_text)
        if match:
            username = match.group(0)
            try:
                user = await event.client.get_entity(username)
            except Exception:
                pass

    if not username:
        return await edit_delete(event, "᯽︙يجب كتابة أو الرد على يوزر حقيقي")

    msg = await edit_or_reply(event, "᯽︙...")

    chat = "@i1wbot"
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/check {username}")
        except YouBlockedUserError:
            return await edit_delete(msg, "᯽︙رجاءً أزل الحظر عن @SangMataInfo_bot")

        responses = []
        ignore_first = True
        while True:
            try:
                response = await conv.get_response(timeout=2)
                if ignore_first:
                    ignore_first = False
                    continue
                responses.append(response.text)
            except asyncio.TimeoutError:
                break

        await event.client.send_read_acknowledge(chat)

    if not responses:
        return await edit_delete(msg, "᯽︙لا توجد نتائج من البوت")

    final_result = "\n\n".join(responses)
    await msg.edit(f"📄︙النتيجة:\n\n{final_result}", parse_mode=_format.parse_pre)

