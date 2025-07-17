from JoKeRUB import l313l
from telethon import events
from telethon.tl.functions.messages import GetMessagesRequest
from telethon.tl.types import DocumentAttributeVideo
import os

@l313l.on(events.NewMessage(pattern=r'^\.((?:حفظ|احفظ)) (https?://[^\s]+)$', outgoing=True))
async def save_from_link(event):
    link = event.pattern_match.group(2)

    try:
        if "/c/" in link:
            # قناة خاصة
            parts = link.split("/")
            chat_id = int("-100" + parts[-2])
            msg_id = int(parts[-1].split("?")[0])
        else:
            # قناة عامة
            parts = link.split("/")
            username = parts[-2]
            msg_id = int(parts[-1].split("?")[0])
            entity = await l313l.get_entity(username)
            chat_id = entity.id

        msg = (await l313l(GetMessagesRequest(chat_id, [msg_id]))).messages[0]

        sent_msg = await event.reply("📥 جاري تحميل المنشور ...")

        if msg.media:
            file_path = await l313l.download_media(msg, file_name="temp")
            kwargs = {
                "file": file_path,
                "caption": msg.text or "",
                "reply_to": event.id
            }

            if hasattr(msg.media, "document") and msg.media.document:
                for attr in msg.media.document.attributes:
                    if isinstance(attr, DocumentAttributeVideo):
                        kwargs["supports_streaming"] = True

            await l313l.send_file(event.chat_id, **kwargs)
            os.remove(file_path)
        elif msg.text:
            await event.reply(msg.text)

        await sent_msg.delete()

    except Exception as e:
        await event.reply(f"❌ خطأ أثناء الحفظ:\n`{e}`")
