import asyncio
from telethon import events, types
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream, InputStream
from JoKeRUB import l313l  # إدارة البوت والجلسة

# ================= إنشاء المكالمات الصوتية =================
pytgcalls = PyTgCalls(l313l.client)

# ================= إدارة الجلسات =================
sessions_info = {}  # كل مجموعة لها سجلها الخاص

# ================= التعامل مع الرسائل =================
@l313l.client.on(events.NewMessage)
async def handler(event):
    chat_id = event.chat_id

    if chat_id not in sessions_info:
        sessions_info[chat_id] = {
            "last_audio": None,
            "voice_chat_id": chat_id,
        }

    session = sessions_info[chat_id]

    # إذا كانت الرسالة صوتية أو ملف صوتي
    if event.message.media and isinstance(event.message.media, types.MessageMediaDocument):
        file_path = await l313l.client.download_media(event.message, f'audio_{chat_id}.mp3')
        session["last_audio"] = file_path
        await event.reply("✅ تم حفظ الصوت! يمكنك كتابة `.شغلها` لتشغيله بالمكالمة.")

    # إذا كتبت .شغلها
    elif event.raw_text.lower() == ".شغلها":
        if session["last_audio"]:
            try:
                await pytgcalls.join_group_call(
                    session["voice_chat_id"],
                    InputStream(InputAudioStream(session["last_audio"]))
                )
                await event.reply("▶️ تم تشغيل الصوت بالمكالمة!")
            except Exception as e:
                await event.reply(f"❌ حدث خطأ أثناء تشغيل الصوت: {e}")
        else:
            await event.reply("❌ لا يوجد صوت محفوظ لتشغيله.")


