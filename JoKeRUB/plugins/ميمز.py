#all write Codes By Team Aljoker @jepthon
#By Hussein @lMl10l
import asyncio
import random
import re
import json
import base64
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from asyncio.exceptions import TimeoutError
from telethon import events
from ..sql_helper.memes_sql import get_link, add_link, delete_link, BASE, SESSION, AljokerLink
from telethon.errors.rpcerrorlist import YouBlockedUserError
#ياقائم آل محمد
from JoKeRUB import l313l
from ..helpers.utils import reply_id
plugin_category = "tools"
# الي يخمط ويكول من كتابتي الا امه انيجه وقد اعذر من انذر
@l313l.on(admin_cmd(outgoing=True, pattern="زيج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/SEFHELLAS/312"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="احبك مصطفى$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/12"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="بلتفك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/7"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انا ماشي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/iirrrq/15"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اني شكو$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/my_7_8/4"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انصدمت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/8"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="فك عيوني$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/10"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="امرع$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/13"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="الجبور$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/14"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كرنج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/730"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سيلوش$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/734"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ام لحلقوم$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/737"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شموتك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/738"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="بكيفك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/739"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="نصو$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/741"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="ياهو انت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/745"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="اضحكله$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/NC2CN/751"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1101"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شلخبار$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1103"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شلونك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1105"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="شلونج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1107"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="نتعرف$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1109"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اني معجبه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1112"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="عجبني اراسلك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1114"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="نرتبط$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1116"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="نتزوج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1118"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ترا حبيتك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1120"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="هلكد ثكيل"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1122"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="دز رصيد$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1127"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اريد رصيد$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1129"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ارشقلي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1131"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="ارشق قناتي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"fhttps://t.me/AJSJ36/1133"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="ارشقلي حسابي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1135"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="سويلي تمويل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1137"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

