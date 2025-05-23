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



@l313l.on(admin_cmd(outgoing=True, pattern="غنيله$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/3184"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
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




@l313l.on(admin_cmd(outgoing=True, pattern="دز صورتك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1139"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="دز ببجي"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1141"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="دز لودو$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1143"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="حساب انستا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1145"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="حساب تيك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1147"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="الو$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1154"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="وينك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1156"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="وينج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1158"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1160"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="لا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1162"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="اكل خره$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1164"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اكلي خره$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1166"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="يله$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1170"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="شبيك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1172"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شبيج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1174"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="احبك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1176"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="احبج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1178"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="تحبني$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1180"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@l313l.on(admin_cmd(outgoing=True, pattern="انطي بوسه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1182"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ابوسك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1189"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="احضنك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1191"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="اريدك بس الي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1194"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()






@l313l.on(admin_cmd(outgoing=True, pattern="ماكدر تصال$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1196"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ماحب لتصال$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1197"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هاي احسن$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1199"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="يلا لتلح$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1203"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@l313l.on(admin_cmd(outgoing=True, pattern="لا تلحين$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1205"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="امداك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1207"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="امداج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1209"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="تمام$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1212"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو محمد$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/3145"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="باي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1213"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="مابيه شي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1217"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="منو$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1219"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كول$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1237"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اكلج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1239"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كولي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1242"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="مبي شحن$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1243"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@l313l.on(admin_cmd(outgoing=True, pattern="من بغداد$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1245"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="من الكوت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1247"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="من لعماره$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1249"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="من الناصريه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1251"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()





@l313l.on(admin_cmd(outgoing=True, pattern="من البصره$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1253"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="من الديوانيه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1255"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="من الحله$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1257"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="من السماوه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1259"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()





@l313l.on(admin_cmd(outgoing=True, pattern="من كربلاء$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1261"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="من النجف$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1263"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="من دبالى$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1265"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="من صلاح الدين$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1267"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@l313l.on(admin_cmd(outgoing=True, pattern="من كركوك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1269"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="من الموصل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1271"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="من سليمانيه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1273"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="من اربيل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1275"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="من دهوك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1277"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="فعلي مميز$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1281"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="بوسهه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1283"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="افتح كام$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1285"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="دز شدات$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1288"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شنو$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1289"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="عرفني عليك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1291"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="وانته$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1293"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="ها$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1295"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شتريد$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1297"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اني بنيه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1306"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="اني بنيه لج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1308"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="17$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1310"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="18$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1315"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="19$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1316"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="20$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1318"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="21$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1320"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="22$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1322"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ها كبينه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1324"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="وين مختفي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1328"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="ثقفو$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1330"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="جبتك لحاله$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1332"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ارجع للمطبخ$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1334"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="شلونكم$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1338"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@l313l.on(admin_cmd(outgoing=True, pattern="ليش$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1221"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="تعذرني$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1223"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="لا شكرا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1225"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة


@l313l.on(admin_cmd(outgoing=True, pattern="باي حبيبي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1227"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="غير مره$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1229"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اكره ليرد متاخر$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1231"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@l313l.on(admin_cmd(outgoing=True, pattern="اكلك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/1235"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

