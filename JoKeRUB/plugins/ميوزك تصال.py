# JoKeRUB Music Voice Plugin — يشغّل البصمات في المكالمة (نهائي)
# ----------------------------------------------------------------
# هذا بلَغ‑إن جاهز لسورس JoKeRUB ويستخدم الكلاينت:
#   from JoKeRUB import l313l
# الأوامر (كلّها تعتمد على الرد على بصمة/ملف صوتي):
#   .شغلها  — يشغّل البصمة المردود عليها في مكالمة الكروب (ويضيف للطابور إذا كان يشغّل حالياً)
#   .ايقاف  — يوقف ويترك المكالمة
#   .تخطي   — يتخطّى للتالية إذا بالطابور، أو يقطع إذا ماكو طابور
# المتطلبات:  pip install pytgcalls
#            (وتأكد FFmpeg مثبت على جهازك)
# التركيب: ضع هذا الملف داخل مجلد الإضافات في JoKeRUB (مثلاً plugins/music_voice.py) وشغّل السورس.

from __future__ import annotations
import asyncio
import tempfile
from dataclasses import dataclass, field
from typing import Deque, Dict, Optional
from collections import deque

from telethon import events
from telethon.tl import types
from JoKeRUB import l313l  # الكلاينت الجاهز

from pytgcalls import PyTgCalls
try:
    from pytgcalls.types import AudioPiped
except Exception:
    AudioPiped = None

# ---------------- PyTgCalls binding ----------------
call = PyTgCalls(l313l)

async def _ensure_started():
    try:
        await call.start()
    except Exception:
        pass

async def _is_voice_or_audio(msg) -> bool:
    if not msg or not msg.media:
        return False
    doc = getattr(msg.media, "document", None)
    if not doc:
        return False
    for attr in getattr(doc, "attributes", []) or []:
        if isinstance(attr, types.DocumentAttributeAudio):
            return True
    return False

async def _download_to_temp(msg) -> str:
    # نحاول اختيار لاحقة مناسبة، بس FFmpeg يقدر يتعامل مع ogg غالباً
    suffix = ".ogg"
    try:
        mt = (getattr(msg, "file", None) and msg.file.mime_type) or ""
        if "mpeg" in mt:
            suffix = ".mp3"
        elif "x-m4a" in mt or "mp4" in mt:
            suffix = ".m4a"
        elif "wav" in mt:
            suffix = ".wav"
        elif "ogg" in mt or "opus" in mt:
            suffix = ".ogg"
    except Exception:
        pass
    f = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    f.close()
    await l313l.download_media(msg, file=f.name)
    return f.name

async def _join_or_change_stream(chat_id: int, src_path: str) -> bool:
    await _ensure_started()
    # جرّب تغيير الستريم إذا متصل، وإلا انضم
    try:
        if hasattr(call, "change_stream"):
            if AudioPiped is not None:
                await call.change_stream(chat_id, AudioPiped(src_path))
            else:
                await call.change_stream(chat_id, src_path)
            return True
    except Exception:
        pass
    try:
        if hasattr(call, "join_group_call"):
            if AudioPiped is not None:
                await call.join_group_call(chat_id, AudioPiped(src_path))
            else:
                await call.join_group_call(chat_id, src_path)
            return True
    except Exception:
        pass
    # بعض الإصدارات القديمة فيها play(chat_id, url)
    try:
        await call.play(chat_id, src_path)
        return True
    except Exception:
        return False

async def _leave_or_stop(chat_id: int) -> bool:
    for m in ("leave_group_call", "leave_call", "stop"):
        if hasattr(call, m):
            try:
                await getattr(call, m)(chat_id)
                return True
            except Exception:
                pass
    return False

# ---------------- حالة الطابور لكل كروب ----------------
@dataclass
class Player:
    chat_id: int
    queue: Deque[str] = field(default_factory=deque)  # مسارات ملفات محلية مؤقتة
    playing: Optional[str] = None
    lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def play_next(self, event):
        async with self.lock:
            if self.playing is not None:
                return
            if not self.queue:
                await event.reply("🎶 الطابور فارغ.")
                return
            self.playing = self.queue.popleft()
            ok = await _join_or_change_stream(self.chat_id, self.playing)
            if ok:
                await event.reply("▶️ تشغيل التالي.")
            else:
                self.playing = None
                await event.reply("❌ ما قدرنا نشغّل.")

players: Dict[int, Player] = {}

def get_player(chat_id: int) -> Player:
    if chat_id not in players:
        players[chat_id] = Player(chat_id)
    return players[chat_id]

# ---------------- الأوامر العربية المعتمدة على الرد ----------------
@l313l.on(events.NewMessage(pattern=None))
async def voice_control_router(event):
    if not event.is_group:
        return
    txt = (event.raw_text or "").strip()

    # .شغلها — لازم رد على بصمة/ملف صوتي
    if txt == ".شغلها":
        if not event.is_reply:
            return await event.reply("↩️ رد على بصمة/ملف صوتي ثم اكتب .شغلها")
        r = await event.get_reply_message()
        if not await _is_voice_or_audio(r):
            return await event.reply("❗ لازم ترد على بصمة/ملف صوتي.")
        path = await _download_to_temp(r)
        player = get_player(event.chat_id)
        # إذا في تشغيل حالي، نضيف للطابور؛ غير ذلك نشغّل مباشرة
        if player.playing is None:
            ok = await _join_or_change_stream(event.chat_id, path)
            if ok:
                player.playing = path
                await event.reply("▶️ تشغيل البصمة بالمكالمة.")
            else:
                await event.reply("❌ فشل تشغيل البصمة.")
        else:
            player.queue.append(path)
            await event.reply("➕ أُضيفت البصمة للطابور.")
        return

    # .ايقاف — خروج من المكالمة ومسح الحالة
    if txt == ".ايقاف":
        await _leave_or_stop(event.chat_id)
        p = players.get(event.chat_id)
        if p:
            p.playing = None
            p.queue.clear()
        return await event.reply("⏹️ تم الإيقاف والخروج.")

    # .تخطي — انتقل للي بعدها إن وجِدت، وإلا اقطع البث
    if txt == ".تخطي":
        player = get_player(event.chat_id)
        player.playing = None
        if player.queue:
            return await player.play_next(event)
        await _leave_or_stop(event.chat_id)
        return await event.reply("⏭️ تم التخطي/القطع.")
