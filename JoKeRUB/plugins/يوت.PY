import asyncio
from telethon import events
from JoKeRUB import l313l  # جلسة سورسك
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream

# ربط PyTgCalls ويا Telethon
pytg = PyTgCalls(l313l)

# قائمة الكروبات المفعلة
target_chats = []

# تفعيل
@l313l.on(events.NewMessage(pattern=r"^\.تفعيل البصمه$"))
async def activate_voice(event):
    global target_chats
    sender = await event.get_sender()
    if not sender or not sender.is_self:
        return

    chat = await event.get_chat()
    chat_id_str = str(chat.id)
    if chat_id_str not in target_chats:
        target_chats.append(chat_id_str)
        await event.reply("✅ تم تفعيل تشغيل البصمات في هذا الكروب.")
    else:
        await event.reply("⚠️ هذا الكروب مفعّل مسبقاً.")

# إيقاف
@l313l.on(events.NewMessage(pattern=r"^\.ايقاف$"))
async def stop_voice(event):
    global target_chats
    sender = await event.get_sender()
    if not sender or not sender.is_self:
        return

    chat = await event.get_chat()
    chat_id_str = str(chat.id)
    if chat_id_str in target_chats:
        target_chats.remove(chat_id_str)
        await event.reply("❌ تم إيقاف تشغيل البصمات في هذا الكروب.")
    else:
        await event.reply("⚠️ هذا الكروب ليس مفعّل.")

# أمر تشغيل البصمة
@l313l.on(events.NewMessage(pattern=r"^\.شغلها$"))
async def play_voice(event):
    global target_chats
    chat = await event.get_chat()
    chat_id_str = str(chat.id)

    if chat_id_str not in target_chats:
        return  # الكروب غير مفعّل

    if not event.reply_to_msg_id:
        await event.reply("⚠️ لازم ترد على بصمة.")
        return

    reply_msg = await event.get_reply_message()
    if not (reply_msg.voice or reply_msg.audio):
        await event.reply("⚠️ الرسالة مو بصمة.")
        return

    try:
        file = await reply_msg.download_media()
        await pytg.join_group_call(
            event.chat_id,
            InputAudioStream(file)
        )
        await event.reply("🎶 تم تشغيل البصمة بالكول!")
    except Exception as e:
        await event.reply(f"❌ خطأ: {e}")

# تشغيل المكتبتين
pytg.start()
l313l.run_until_disconnected()
