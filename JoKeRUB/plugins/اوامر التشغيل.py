import sys
import glob
import os
import re
import shlex
from asyncio.exceptions import CancelledError
from time import sleep
import asyncio
from JoKeRUB import l313l
from telethon import events
from ..core.logger import logging
from ..core.managers import edit_or_reply, edit_delete
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, HEROKU_APP
from ..helpers.utils import _catutils

LOGS = logging.getLogger(__name__)
plugin_category = "tools"

JOKRDEV = [1374312239, 393120911, 1490479382, 5564802580]

# ===============================================================

def _get_cfg(key: str, default: str = None):
    """يقرأ إعداد من env ثم gvar ثم default."""
    return os.getenv(key) or gvarstatus(key) or default

async def aljoker_4ever():
    """
    يحدث السورس عبر git clone من GitHub (إلزامي) في مجلد مؤقت TempCat،
    ينقل الملفات إلى مجلد التشغيل الحالي (بدون مسار ثابت)،
    يثبت المتطلبات، يفعّل venv، ثم يشغّل البوت.
    """
    # 1) تحديد مسار التشغيل الديناميكي (المجلد الحالي)
    run_dir = os.getcwd()
    run_dir_q = shlex.quote(run_dir)

    # 2) إعدادات الريبو/الفرع
    repo_url = _get_cfg("JOKER_REPO_URL", None)
    if not repo_url:
        gh_owner = _get_cfg("JOKER_GH_OWNER", "aesareetcuu6jllk")
        repo_name = _get_cfg("JOKER_REPO", "algokkkarrr1222")
        repo_url = f"https://github.com/{gh_owner}/{repo_name}.git"
    branch = _get_cfg("JOKER_BRANCH", "HuRe")

    # 3) git clone إلى TempCat داخل مجلد التشغيل الحالي
    await _catutils.runcmd(
        "bash -lc '"
        f"cd {run_dir_q} && "
        "rm -rf TempCat && "
        f"git clone -b {shlex.quote(branch)} {shlex.quote(repo_url)} TempCat'"
    )

    # 4) نقل الملفات من TempCat إلى مجلد التشغيل
    # - نتجنب نقل .git و .venv حتى لا نخرب بيئة التشغيل
    await _catutils.runcmd(
        "bash -lc '"
        f"cd {run_dir_q} && "
        "shopt -s dotglob && "
        "for f in TempCat/*; do "
        "  base=\"$(basename \"$f\")\"; "
        "  if [ \"$base\" != \".git\" ] && [ \"$base\" != \".venv\" ]; then "
        "    rm -rf \"$base\"; "
        "    mv \"$f\" ./; "
        "  fi; "
        "done && "
        "rm -rf TempCat'"
    )

    # 5) تثبيت المتطلبات الأساسية (خارج venv لضمان توافر الأدوات)
    await _catutils.runcmd(
        "bash -lc '"
        f"cd {run_dir_q} && "
        "if [ -f requirements.txt ]; then python3 -m pip install --no-cache-dir -r requirements.txt || true; fi'"
    )

    # 6) تنظيف أثر قديم إن وُجد
    if os.path.exists(os.path.join(run_dir, "jepvc")):
        await _catutils.runcmd(f"bash -lc 'cd {run_dir_q} && rm -rf jepvc'")

    # 7) تهيئة وتشغيل داخل venv + تحديث submodules + تشغيل JoKeRUB
    cmd = (
        "bash -lc '"
        f"cd {run_dir_q} && "
        "(command -v deactivate >/dev/null 2>&1 && deactivate || true) && "
        "python3 -m venv .venv && "
        "source .venv/bin/activate && "
        "git pull --recurse-submodules && "
        "git submodule update --init --recursive && "
        "python3 -m pip install -U pip && "
        "(python3 -m pip uninstall -y JoKeRUB >/dev/null 2>&1 || true) && "
        "python3 -m pip install -r requirements.txt && "
        'export PYTHONPATH=\"$PWD\" && '
        "python -m JoKeRUB'"
    )
    await _catutils.runcmd(cmd)

@l313l.ar_cmd(
    pattern="تحديث",
    command=("تحديث", plugin_category),
    info={
        "header": "To reload your bot in vps/ similar to restart",
        "flags": {
            "re": "restart your bot without deleting junk files",
            "clean": "delete all junk files & restart",
        },
        "usage": [
            "{tr}reload",
            "{tr}cleanload",
        ],
    },
)
async def cmd_reload(event):
    "To reload Your bot"
    joker = await edit_or_reply(event, "** ᯽︙ انتظر 2-3 دقيقة, جارِ اعادة التشغيل...**")
    await aljoker_4ever()
    await event.client.reload(joker)

@l313l.ar_cmd(
    pattern="اطفاء$",
    command=("اطفاء", plugin_category),
    info={
        "header": "Shutdowns the bot !!",
        "description": "To turn off the dyno of heroku. you cant turn on by bot you need to got to heroku and turn on or use @hk_heroku_bot",
        "usage": "{tr}shutdown",
    },
)
async def cmd_shutdown(event):
    "Shutdowns the bot"
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "**᯽︙ إيقاف التشغيـل ✕ **\n**᯽︙ تـم إيقـاف تشغيـل البـوت بنجـاح ✓**"
        )
    await edit_or_reply(
        event,
        "**᯽︙ جـاري إيقـاف تشغيـل البـوت الآن ..**\n"
        "᯽︙  **أعـد تشغيـلي يدويـاً لاحقـاً عـبر هيـروڪو ..**\n"
        "⌔︙**سيبقى البـوت متوقفـاً عن العمـل**"
    )
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)

@l313l.ar_cmd(
    pattern="التحديثات (تشغيل|ايقاف)$",
    command=("التحديثات", plugin_category),
    info={
        "header": "᯽︙ لتحديـث الدردشـة بعـد إعـادة التشغيـل  أو إعـادة التحميـل  ",
        "description": "⌔︙سيتـم إرسـال بنـك cmds ڪـرد على الرسالـة السابقـة الأخيـرة لـ (إعادة تشغيل/إعادة تحميل/تحديث cmds) 💡.",
        "usage": [
            "{tr}التحديثات <تشغيل/ايقاف",
        ],
    },
)
async def set_pmlog(event):
    "᯽︙ لتحديـث الدردشـة بعـد إعـادة التشغيـل  أو إعـادة التحميـل  "
    input_str = event.pattern_match.group(1)
    if input_str == "ايقاف":
        if gvarstatus("restartupdate") is None:
            return await edit_delete(event, "**᯽︙ تـم تعطيـل التـحديـثات بالفعـل ❗️**")
        delgvar("restartupdate")
        return await edit_or_reply(event, "**⌔︙تـم تعطيـل التـحديـثات بنجـاح ✓**")
    if gvarstatus("restartupdate") is None:
        addgvar("restartupdate", "turn-oned")
        return await edit_or_reply(event, "**⌔︙تـم تشغيل التـحديـثات بنجـاح ✓**")
    await edit_delete(event, "**᯽︙ تـم تشغيل التـحديـثات بالفعـل ❗️**")

# ملاحظة: عدم تكرار نفس الاسم
@l313l.on(events.NewMessage(incoming=True))
async def dev_control_reload(event):
    if event.reply_to and event.sender_id in JOKRDEV:
        reply_msg = await event.get_reply_message()
        owner_id = getattr(reply_msg.from_id, "user_id", getattr(reply_msg, "from_id", None))
        if owner_id == l313l.uid:
            if event.message.message.strip() == "اعادة تشغيل":
                joker = await event.reply("** ᯽︙ بالخدمة مطوري سيتم اعادة تشغيل السورس 😘..**")
                await aljoker_4ever()
                await event.client.reload(joker)

@l313l.on(events.NewMessage(incoming=True))
async def dev_control_shutdown(event):
    if event.reply_to and event.sender_id in JOKRDEV:
        reply_msg = await event.get_reply_message()
        owner_id = getattr(reply_msg, "from_id", None)
        if owner_id == l313l.uid:
            if event.message.message.strip() == "اطفاء":
                await event.reply("**᯽︙ تدلل مولاي تم اطفاء السورس بواسطة تاج راسك 😁**")
                if HEROKU_APP is not None:
                    HEROKU_APP.process_formation()["worker"].scale(0)
                else:
                    sys.exit(0)
