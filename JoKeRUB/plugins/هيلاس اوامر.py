import re

from telethon import Button, events
from telethon.events import CallbackQuery

from l313l.razan.resources.assistant import *
from l313l.razan.resources.mybot import *
from JoKeRUB import l313l
from ..core import check_owner
from ..Config import Config

# نصوص محتويات كل زر (يمكن تعديل النصوص حسب طلبك)

###هيلاس 
l313l0 = """** قائمة اوامر الادمن لسورس HELLAS  **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحظر` )\n- ( `.اوامر الكتم` )\n- ( `.اوامر التثبيت` )\n- ( `.اوامر الاشراف` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""

rozbot  = """** قائمة اوامر المجـموعه لسورس HELLAS  **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التفليش` )\n- ( `.اوامر المحذوفين` )\n- ( `.اوامر الكروب` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
gro = """** قائمة اوامر الـترحيب والـردود **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترحيب` )\n- ( `.اوامر الردود` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
grrz = """** قائمة اوامر حـماية الخاص والتلكراف **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحماية` )\n- ( `.اوامر التلكراف` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
r7brz = """ ** قائمة اوامر المساعدة  **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الوقت والتاريخ` )\n- ( `.اوامر كورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر مساعدة` )\n- ( `.اوامر الاذاعه` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
jrzst = """ ** قائمة اوامر التكرار والتنظيف **:\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التكرار` )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
rfhrz = """ **⦑ قائمة الأوامر الجديدة ⦒**\n"
            "★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n"
            "⥾ `.اوامر البصمات`\n"
            "⥾ `.اوامر النقل`\n"
            "⥾ `.اوامر الرصيد`\n"
	    "⥾ `.اوامر النشر`\n"
            "⥾ `.اوامر التنزيل`\n"
            "⥾ `.اوامر الذكاء`\n"
            "★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n"
            "⌔︙CH : @HELLASUserBot"""
uscuxrz = """** قائمة اوامر الـمنشن والانتحال **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot """
Jmrz = """ ** قائمة اوامر الحساب و الترفيه **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترفيه` )\n- ( `.اوامر الحساب` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
sejrz = """ ** قائمة اوامر تحويل الصيغ و الجهات **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
krrznd1 = """ ** قائمة اوامر الملصقات وكوكل **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر كوكل` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
krrznd = """ ** قائمة اوامر الوقتي والتشغيل **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الاسم` )\n- ( `.اوامر البايو` )\n- ( `.اوامر الكروب الوقتي` )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
tslrzj = """ ** قائمة اوامر التسلية والتحشيش **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n- ( `.اوامر الميمز` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
iiers = """ ** قائمة اوامر تجميع النقاط و بوت وعد **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التجميع` ) \n- ( `.اوامر وعد` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBoT"""

ROE = "**♰ هـذه هي قائمة اوامـر سـورس 𝐇𝐞𝐥𝐥𝐚𝐬  ♰**"
JEP_IC = ""  # ضع مسار صورة هنا إذا تريد

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
  
   @tgbot.on(events.InlineQuery)
   async def inline_handler(event):
    builder = event.builder
    result = None
    query = event.text
    await bot.get_me()
    if query.startswith("اوامر هيلاس") and event.query.user_id == bot.uid:
        buttons = [
    [Button.inline("  اوامر الادمن ", data="l313l0")],  # زر واحد
    [Button.inline("  اوامر المجموعة ", data="rozbot"), Button.inline("  اوامر الحساب والترفيه ", data="Jmrz")],
    [Button.inline(" اوامر الترحيب والردود ", data="gro"), Button.inline(" اوامر الصيغ والجهات ", data="sejrz")],
    [Button.inline("  حماية خاص والتلكراف ", data="grrz"), Button.inline("  اوامر التسلية والميمز ", data="tslrzj")],
    [Button.inline("  اوامر المساعدة والإذاعة ", data="r7brz"), Button.inline("  اوامر المـلصقات وكوكل ", data="krrznd1")],
    [Button.inline("  اوامر التنظيف والتكرار ", data="jrzst"), Button.inline("  اوامر الوقتي و التشغيل ", data="krrznd")],
    [Button.inline("  اوامر اضافيه للسورس ", data="rfhrz"), Button.inline("  اوامر تجميع النقاط وبوت وعد ", data="iiers")],
    [Button.inline(" اوامر المنشن والانتحال ", data="uscuxrz")],  # زر واحد
]

        if JEP_IC and JEP_IC.endswith((".jpg", ".png", "gif", "mp4")):
            result = builder.photo(
                JEP_IC, text=ROE, buttons=buttons, link_preview=False
            )
        elif JEP_IC:
            result = builder.document(
                JEP_IC,
                title="JoKeRUB",
                text=ROE,
                buttons=buttons,
                link_preview=False,
            )
        else:
            result = builder.article(
                title="JoKeRUB",
                text=ROE,
                buttons=buttons,
                link_preview=False,
            )
        await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="اوامر هيلاس"))
async def repo(event):
    if event.fwd_from:
        return
    F_O_1 = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(F_O_1, "اوامر هيلاس")
    await response[0].click(event.chat_id)
    await event.delete()


# هنا دوال الرد على كل زر مع النصوص وملاحة بين الصفحات

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"l313l0")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="rozbot"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(l313l0, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rozbot")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="gro"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(rozbot, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"gro")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="grrz"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(gro, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"grrz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="r7brz"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(grrz, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"r7brz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="jrzst"),
          Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(r7brz, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"jrzst")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="rfhrz"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(jrzst, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rfhrz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="uscuxrz"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(rfhrz, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"uscuxrz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="Jmrz"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(uscuxrz, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Jmrz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="sejrz"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(Jmrz, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"sejrz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="tslrzj"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(sejrz, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"tslrzj")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="krrznd1"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(tslrzj, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"krrznd1")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="krrznd"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(krrznd1, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"iiers")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(iiers, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"CLORN")))
@check_owner
async def _(event):
    # زر القائمة الرئيسية يعيدك للنص الأساسي مع زر التنقل
    buttons = [
    [Button.inline(" اوامر الادمن ", data="l313l0")],  # زر واحد
    [Button.inline(" اوامر المجموعة ", data="rozbot"), Button.inline("  اوامر الحساب والترفيه ", data="Jmrz")],
    [Button.inline("اوامر الترحيب والردود ", data="gro"), Button.inline("  اوامر الصيغ والجهات ", data="sejrz")],
    [Button.inline(" حماية خاص والتلكراف ", data="grrz"), Button.inline("  اوامر التسلية والميمز ", data="tslrzj")],
    [Button.inline(" اوامر المساعدة والإذاعة ", data="r7brz"), Button.inline("  اوامر المـلصقات وكوكل ", data="krrznd1")],
    [Button.inline(" اوامر التنظيف والتكرار ", data="jrzst"), Button.inline("  اوامر الوقتي و التشغيل ", data="krrznd")],
    [Button.inline("  اوامر اضافيه للسورس ", data="rfhrz"), Button.inline(" اوامر تجميع النقاط وبوت وعد ", data="iiers")],
    [Button.inline("  اوامر المنشن والانتحال ", data="uscuxrz")], 
]
    await event.edit(ROE, buttons=buttons)
