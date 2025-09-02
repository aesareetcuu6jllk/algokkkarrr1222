# JoKeRUB Music Voice Plugin — كامل مكمل
# -------------------------------------------------------------
# بلَغ‑إن ميوزك جاهز لسورس JoKeRUB، يشتغل مع الكلاينت:
#   from JoKeRUB import l313l
#
# الأوامر:
#   .شغلها  — رد على بصمة/ملف صوتي لتشغيله في المكالمة (إذا أكو تشغيل يضيفها للطابور)
#   .ايقاف  — يوقف التشغيل ويترك المكالمة
#   .تخطي   — يتخطى للتالية أو يقطع إذا الطابور فاضي
#   .طابور  — يعرض الطابور الحالي
#
# المتطلبات:
#   pip install telethon pytgcalls tgcalls==2.0.0
#   sudo apt-get install -y ffmpeg
#
# ضع الملف داخل مجلد plugins/ في JoKeRUB وشغّل السورس.
import plugins.music_voice
import asyncio, tempfile
from dataclasses import dataclass, field
from typing import Deque, Dict, Optional
from collections import deque

from telethon import events
from telethon.tl import types
from JoKeRUB import l313l

from pytgcalls import PyTgCalls
try:
    from pytgcalls.types import AudioPiped
except Exception:
    AudioPiped = None

# ---------------- ربط المكالمات ----------------
call = PyTgCalls(l313l)

async def _ensure_started():
    try:
        await call.start()
    except Exception:
        pass

async def _is_voice(msg) -> bool:
    if not msg or not msg.media:
        return False
    doc = getattr(msg.media, "document", None)
    if not doc:
        return False
    for attr in getattr(doc, "attributes", []) or []:
        if isinstance(attr, types.DocumentAttributeAudio):
            return True
    return False

async def _download_temp(msg) -> str:
    suffix = ".ogg"
    mt = (getattr(msg, "file", None) and msg.file.mime_type) or ""
    if "mpeg" in mt: suffix = ".mp3"
    elif "x-m4a" in mt or "mp4" in mt: suffix = ".m4a"
    elif "wav" in mt: suffix = ".wav"
    f = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    f.close()
    await l313l.download_media(msg, file=f.name)
    return f.name

async def _join_or_stream(chat_id: int, src: str) -> bool:
    await _ensure_started()
    try:
        if hasattr(call, "change_stream"):
            if AudioPiped: await call.change_stream(chat_id, AudioPiped(src))
            else: await call.change_stream(chat_id, src)
            return True
    except: pass
    try:
        if hasattr(call, "join_group_call"):
            if AudioPiped: await call.join_group_call(chat_id, AudioPiped(src))
            else: await call.join_group_call(chat_id, src)
            return True
    except: pass
    try:
        await call.play(chat_id, src)
        return True
    except: return False

async def _leave(chat_id: int):
    for m in ("leave_group_call", "leave_call", "stop"):
        if hasattr(call, m):
            try:
                await getattr(call, m)(chat_id)
                return True
            except: pass
    return False

# ---------------- إدارة الطابور ----------------
@dataclass
class Player:
    chat_id: int
    queue: Deque[str] = field(default_factory=deque)
    playing: Optional[str] = None
    lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def play_next(self, event):
        async with self.lock:
            if self.playing is not None:
                return
            if not self.queue:
                await event.reply("🎶 الطابور فارغ."); return
            self.playing = self.queue.popleft()
            ok = await _join_or_stream(self.chat_id, self.playing)
            if ok:
                await event.reply("▶️ تشغيل التالي.")
            else:
                self.playing = None
                await event.reply("❌ فشل التشغيل.")

players: Dict[int, Player] = {}

def get_player(cid: int) -> Player:
    if cid not in players:
        players[cid] = Player(cid)
    return players[cid]

# ---------------- الأوامر ----------------
@l313l.on(events.NewMessage(pattern=None))
async def control(event):
    if not event.is_group: return
    txt = (event.raw_text or "").strip()

    # تيست سريع للتأكد من تحميل البلغ‑إن
    if txt == ".تيست":
        return await event.reply("✅ البلغ‑إن شغّال.")

    if txt == ".شغلها":
        if not event.is_reply:
            return await event.reply("↩️ رد على بصمة")
        r = await event.get_reply_message()
        if not await _is_voice(r):
            return await event.reply("❗ لازم ترد على بصمة")
        path = await _download_temp(r)
        player = get_player(event.chat_id)
        if player.playing is None:
            ok = await _join_or_stream(event.chat_id, path)
            if ok:
                player.playing = path
                await event.reply("▶️ تشغيل البصمة.")
            else:
                await event.reply("❌ فشل التشغيل.")
        else:
            player.queue.append(path)
            await event.reply("➕ أُضيفت للطابور.")
        return

    if txt == ".ايقاف":
        await _leave(event.chat_id)
        p = players.get(event.chat_id)
        if p:
            p.playing = None; p.queue.clear()
        return await event.reply("⏹️ تم الإيقاف.")

    if txt == ".تخطي":
        p = get_player(event.chat_id)
        p.playing = None
        if p.queue:
            return await p.play_next(event)
        await _leave(event.chat_id)
        return await event.reply("⏭️ تم التخطي.")

    if txt == ".طابور":
        p = get_player(event.chat_id)
        now = f"الآن: {p.playing}
" if p.playing else "الآن: —
"
        rest = "
".join([f"{i+1}. {x}" for i,x in enumerate(list(p.queue))]) or "(فارغ)"
        return await event.reply(now+rest)
