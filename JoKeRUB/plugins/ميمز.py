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

@l313l.on(admin_cmd(outgoing=True, pattern="ها يوسف$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/AJSJ36/2430"
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




@l313l.on(admin_cmd(outgoing=True, pattern="عزه العزاك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1431"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="جنك ماعاجبك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1433"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شكد سخيف$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1436"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انت مطي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1438"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شكد تحمه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1440"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شكد فكر$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1443"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شكد فطير$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1445"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شكد فاهي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1447"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شكد غبي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1449"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شنو اسمج$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1451"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شكرا$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1453"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو كرار$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1457"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="امحح$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1459"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كافي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1461"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ماتاكل خره$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1463"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ايع$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1465"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انجب$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1467"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="وي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1469"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="فهمت لو لا$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1471"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="عادي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1473"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="امحححح$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1475"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو ابراهيم$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1477"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو حيدر$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1479"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو رضا$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1481"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو مرتضى$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1483"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو عمر$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1485"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اخوي جفت$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1490"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="والله تمام$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1492"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اني بخير$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1496"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="الو السلام$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1498"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انته طيري$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1500"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="وسام احبك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1530"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="هلو سجاد$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1408"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو باقر$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1410"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو زيد$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1412"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شدتسوي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1419"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ليش زعلت$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1421"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شكد عمرك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1423"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شكد تحبني$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1425"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ضفي النيه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1427"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ضحكه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1429"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="شتريد يسولفون$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1385"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="بنيه تره$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1388"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="لتصير تافه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1390"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو عبد$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1392"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو علي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1396"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو حسون$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1398"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو حسين$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1400"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو مصطفى$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1404"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو احمد$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1406"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="شوف اغار$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1363"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اغار عليك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1364"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="غزل$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1366"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="وصخ$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1350"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="دي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1352"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اتسرسح$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1354"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="تحبيني$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1359"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اموت عليك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1361"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ماريد اغلط$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1340"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ماريد اهينك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1342"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ماريد اهينج$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1344"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انجب$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1346"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انجبي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1348"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="انت لمالك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1542"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ارفعني$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = "https://t.me/AJSJ36/1544"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="تصبحون على خير$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1546"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اجت فكره$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1558"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="تموت عل بنات$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1560"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو مسلم$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1572"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="السلام$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1650"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ممكن نتعرف$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1652"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اني زينه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1656"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="دز صورتك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1658"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هاي انته$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1660"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="من وين$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1662"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()





@l313l.on(admin_cmd(outgoing=True, pattern="اشكد عمرك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1664"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انت مرتبط$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1666"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="من امت مرتبط$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1668"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ليش مامرتبط$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1670"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="نصير اصدقاء$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1672"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="تشرفت$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1674"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="لحضه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1686"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="مشغول$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1688"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="مترد بسرعه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1690"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="الجو حار$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1692"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()







@l313l.on(admin_cmd(outgoing=True, pattern="شخبارك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1695"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="تابع مردوده$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1701"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اسمي ايه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1706"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ضحكتني$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1708"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="جوعانه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1710"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="امي صاحتني$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1712"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="بابا صاحني$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1714"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اريد اتغده$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1716"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هسه كعدو اهلي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1718"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="صباحو$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1729"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()









@l313l.on(admin_cmd(outgoing=True, pattern="سلام عليكم$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1731"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="عليكم السلام$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1733"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="عليكم السلام تفضلي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1735"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="احبك علي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1739"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="احبك حسين$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1741"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="احبك عباس$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1743"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="مشتاقتلك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1745"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="نسيتني$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1747"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ليش تحظر$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1749"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="احبك اورهان$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f""
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()








@l313l.on(admin_cmd(outgoing=True, pattern="احبك2$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1774"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="عبودي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1776"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ابعت هديه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1778"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="بهاء احبك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1782"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="دز رصيد اونسك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1785"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="فوك ما تعبانه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1789"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ثقه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1790"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="باي تعبت ممستفاده$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1792"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="احبك احمد$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1794"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="مشايف حلوين$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1833"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()








@l313l.on(admin_cmd(outgoing=True, pattern="طفي الكامره$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1834"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="زلمه جيس$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1835"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انجب لدوخني$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1836"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اخجل اني$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1837"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شنو هذه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1838"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اتصنع$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1839"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ماعرف شحجي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1840"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="حشوره$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1841"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="تحب الاندومي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1842"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اكوله احبك يكلي شلابسه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1843"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()







@l313l.on(admin_cmd(outgoing=True, pattern="اوي دروحي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1844"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كتمتك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1845"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هاي شبيك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1846"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="لكلاوات$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1847"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هاي ليش$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1848"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو شلونك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1873"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="عادي نتعرف$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1875"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ااسلام عليكم$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1877"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شلونك2$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1879"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اني سينكل$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1881"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()







@l313l.on(admin_cmd(outgoing=True, pattern="اني حلوه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1883"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اهلي يمي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1887"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="مكدر$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1889"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اهلي ميعرفون$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1891"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="يله تنام$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1917"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="من وين$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1929"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شسمك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1931"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="تشرفت2$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1935"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ببا منطقه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1937"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="مرتبط$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1939"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()







@l313l.on(admin_cmd(outgoing=True, pattern="ما مرتبطه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1941"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ولا مره$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1943"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كم مره حبيت$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1945"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="نت ماعندي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1947"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="طلب$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1951"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="رشق انستا$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1956"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انت تحبني$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1959"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اني احبك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1961"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كم اخ عندك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1963"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="وحيده لهلي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1967"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()






@l313l.on(admin_cmd(outgoing=True, pattern="مخنوكه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1969"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="بيت عمي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1971"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="بيت خالتي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1973"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="بيت عمتي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1975"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="رايحه للطبيب$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1977"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="عادي نرتبط$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1979"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شوي وجي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1981"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="يلا اجيت$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/1983"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اخمطج$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2049"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اني حساسه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2053"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()






@l313l.on(admin_cmd(outgoing=True, pattern="متغيير عليه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2055"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كيفك حبيبي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2057"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلا بروحي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2059"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلو شلونك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2061"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="صور خاصك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2064"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="سلم على امك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2066"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شنو مصدك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2193"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="رفعني$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2195"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="مالك5$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2197"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="وكت ليعجبني ادز$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2199"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()





@l313l.on(admin_cmd(outgoing=True, pattern="اني اتصل$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2203"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="رتبه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2205"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="غزل7$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2240"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ها دوده$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2258"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كس امك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2260"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="تنيجين$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2262"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="تنيج$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2264"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كس امج$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2266"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="دي فرخ$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2268"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كحبه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2270"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()







@l313l.on(admin_cmd(outgoing=True, pattern="ابلع بلوك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2281"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انت الحب$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2283"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انت الاول$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2285"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="وين وصلت$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2301"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ابد لتحاول$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2313"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انت تدبرها$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2319"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انت قافل$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2323"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اعشقك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2327"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اسفا$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2329"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اريد اشوفك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2331"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()








@l313l.on(admin_cmd(outgoing=True, pattern="ليش مصدك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2426"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="غنيلي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2426"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كوه دزيت$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2426"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="حروح اسبح$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2486"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اشكرك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2513"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="نورت$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2515"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="مافهم عليج$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2519"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="جهز رصيدك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2521"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="جيب رصيد$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2523"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="العفو كلبي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/AJSJ36/2527"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
###دجله
@l313l.on(admin_cmd(outgoing=True, pattern="اريد اروح$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/yyegksgfdg/1113"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انجب2$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/yyegksgfdg/1114"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انجبي2$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/yyegksgfdg/1115"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شسمك2$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/yyegksgfdg/1116"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()




###
@l313l.on(admin_cmd(outgoing=True, pattern="من تحول$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/4"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="على شنو$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/6"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هلا تفضل$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/8"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هلا شلونك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/10"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="تمام الحمدلله$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/13"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="واني شعليه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/19"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="حول وريحك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/15"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مواصفات$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/15"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="تمامم$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/20"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="وين مكانك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/22"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="عمولتي10$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/24"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اه مشتهيه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/26"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ماعندك ثقه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/28"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="مو بكيفك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/31"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="جاد لو لا$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/32"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="للثقه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/36"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لاحضرك$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/38"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مالتي وردي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/41"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اخابر وجي$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/43"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="كل لمحافضات$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/44"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اني بنت$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/46"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="تبياته لو ساعات$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/50"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="كام10 صوت5$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/52"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="سعر تبياته$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/61"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="سعر ساعه$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/64"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مكان$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/67"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اعمار$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/bxhbvtujxsrfx/70"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="خره2$"))
async def jepmeme(memejep):
    Jep = await reply_id(memejep)
    url = f"https://t.me/yyegksgfdg/1391"
    await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="مرتبط2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1118"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="لويش مامرتبط$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1119"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="لحضه2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1120"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="عومري$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1146"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="احبك2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1166"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()





@l313l.on(admin_cmd(outgoing=True, pattern="تفاعل قليل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1172"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="احبج2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1266"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="اموت بيك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1268"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="اموت بيج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1269"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()




@l313l.on(admin_cmd(outgoing=True, pattern="حياتي2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1270"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="رويحتي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1271"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="شلونك2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1272"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="شلونج2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1273"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@l313l.on(admin_cmd(outgoing=True, pattern="شخباركم2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1274"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="بخير اذا انت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1275"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="شكو ماكو$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1276"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="بيش$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1277"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="بيش$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1278"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="بصره$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1279"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="بغداد$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1280"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ديالى$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1281"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لحله$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1282"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اربيل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1283"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="كوت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1284"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="سامراء$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1285"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="كوت2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1286"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نورت2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1287"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نورتي2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1288"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="حياك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1289"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="حياج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1290"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مقدمه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1291"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نهايه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1294"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="صباحو2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1295"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مساء الورد$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1296"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هلاةيروحي2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1297"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هلا قلبي2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1298"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="بربوك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1299"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ابلع بلوك2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1301"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شعر1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1302"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شعر2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1303"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="امشي لك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1305"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ابو لبنات$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1306"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete() 
@l313l.on(admin_cmd(outgoing=True, pattern="ايع2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1308"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مشاعرك عضروطيه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1309"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="س ميوزك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1341"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="س نشر$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1342"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="س حمايه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1343"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اريد هديه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1345"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اريد نجوم$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1346"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="50 نجمه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1347"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="100 نجمه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1348"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ماعندي نجوم$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1349"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="25 نجمه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1350"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شلخبار2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1352"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شلونك3$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1353"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شلونج3$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1354"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نتعرف2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1355"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="معجبه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1356"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="عجبني اراسلك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1357"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نرتبط2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1358"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="نزوج2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1359"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ترا حبيتك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1360"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="دز صورتك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1364"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="سويلي تمويل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1365"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ارشق قناتي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1366"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ارشقلي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1367"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="2غنيلي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1368"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="غنيلك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1369"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ارشق حسابي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1370"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="دز رصيد2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1375"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شبيك لك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1392"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ماكدر تصال2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1393"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ماحب لتصال2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1394"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ابوسك2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1395"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="وينك2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1399"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="الو2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1400"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اني بنيه لك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1403"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اني بنيه لج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1404"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مبي شحن2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1406"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="يلا لتلح2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1407"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="يلا لتلحين2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1409"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="مادري2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1410"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="فعلي مميز2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1413"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="همداك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1415"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شدلي منصه2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1420"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="بيش هاذ$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1422"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="قفل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1425"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="متتوفر$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1428"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="الو السلام2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1432"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شكد فاهي2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1433"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شدسوي2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1438"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="انت فاهي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1439"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هاي انته2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1444"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شتريد2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1445"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اني حلوه2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1446"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ارفعني2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1452"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ليش2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1453"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="تعذرني$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1454"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لا شكرا2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1455"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ثقفو2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1456"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="عزه لعزاك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1459"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شكد سخيف2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1466"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لبش تغييرت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1473"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="جنك ماعاجبك2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1474"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اكل خره2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1476"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="اخوي اجهه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1477"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هلو كرار2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1478"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هلو محمد2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1479"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هلو علي2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1480"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هلو داده$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1481"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="عيوني الك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1486"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="شكد عمرك2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1487"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="من شوكت مرتبط$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1488"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="راح احذفك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1489"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="رد خاص$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1490"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="كلشي من وراك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1491"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="لاشوف غيري$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1492"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هواي تعبت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1493"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="ليش زعلت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1494"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هلو حسون2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1495"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هلو عبودي2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1496"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="هلو مصطفى2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f""
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@l313l.on(admin_cmd(outgoing=True, pattern="وصخ2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/yyegksgfdg/1498"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

###ميمز

@l313l.on(admin_cmd(outgoing=True, pattern="هاروني$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/97"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="همبركر$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/98"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="لا شماته$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/4"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="تفضل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/5"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اشكرج طبعا$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/7"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ماردنا الطلايب$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/8"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="موال سلام$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/9"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اف مبروك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/10"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="الاكننا الافضل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/11"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اطلع بره$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/12"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="بليز ترامب$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/13"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="واجب$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/14"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="حيدر كيمز$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/15"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شماته$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/19"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="يلا دي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/21"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="وين كلاوات$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/23"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="لكيتني$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/24"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="يعني يعني$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/25"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="يبو فاضل$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/26"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="جلاب$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/27"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# 10 أخرى أيضاً بنفس الشكل:

@l313l.on(admin_cmd(outgoing=True, pattern="حسناء$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/28"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انت اسكت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/29"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="اسكت ياخي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/30"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ارسلني حمزه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/32"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="عفطه$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/36"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="حيل ضايج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/41"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="شجاي تلغي$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/47"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="كافي جلبت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/48"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="هاي شبيك$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/50"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="انا اسفف$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/kkmgee/53"
  await memejep.client.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()
