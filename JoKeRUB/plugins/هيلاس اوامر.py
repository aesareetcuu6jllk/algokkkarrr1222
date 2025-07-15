import re

from telethon import Button, events
from telethon.events import CallbackQuery

from l313l.razan.resources.assistant import *
from l313l.razan.resources.mybot import *
from JoKeRUB import l313l
from ..core import check_owner
from ..Config import Config

# نصوص محتويات كل زر (يمكن تعديل النصوص حسب طلبك)
ROZADM = """⦑ أوامر الأدمن ⦒
.م1 - أمر 1
.م2 - أمر 2
..."""
GRTSTI = """⦑ أوامر الملصقات وصور ⦒
.ملصق - إرسال ملصق
.صورة - إرسال صورة
..."""
JMAN = """⦑ أوامر التسلية ⦒
.نكتة - إرسال نكتة
.حالة - إرسال حالة
..."""
TKPRZ = """⦑ أوامر التنظيف والتكرار ⦒
.تنظيف - تنظيف المحادثة
.تكرار - تكرار رسالة
..."""
ROZBOT = """⦑ أوامر البوت ⦒
.بوت - معلومات البوت
.تشغيل - تشغيل الموسيقى
..."""
JROZT = """⦑ أوامر الحساب ⦒
.حساب - معلومات الحساب
.رصيد - عرض الرصيد
..."""
JMTRD = """⦑ الترحيبات والردود ⦒
.ترحيب - تعيين ترحيب
.ردود - عرض الردود
..."""
ROZSEG = """⦑ الصيغ والجهات ⦒
.صيغ - تنسيق النصوص
.جهات - إدارة جهات الاتصال
..."""
JMGR1 = """⦑ المجموعات ⦒
.مجموعات - عرض المجموعات
.انضمام - الانضمام لمجموعة
..."""
ROZPRV = """⦑ الحماية والتلكراف ⦒
.قفل - قفل نوع معين
.فتح - فتح نوع معين
..."""
HERP = """⦑ الترفيه ⦒
.لعب - ألعاب ممتعة
.مسابقات - مسابقات يومية
..."""
T7SHIZ = """⦑ الانتحال والتقليد ⦒
.منشن - منشن خاص
.تقليد - تقليد عضو
..."""
CLORN = """⦑ القائمة الرئيسية ⦒
.م1 - اوامر الادمن
.م2 - اوامر المجموعة
.م3 - اوامر الترحيب والردود
...
"""

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
    [Button.inline(" ( .م1 ) ⦙ اوامر الادمن ", data="l313l0")],  # زر واحد
    [Button.inline(" ( .م2 ) ⦙ اوامر المجموعة ", data="rozbot"), Button.inline(" ( .م18 ) ⦙ اوامر الحساب والترفيه ", data="Jmrz")],
    [Button.inline(" ( .م3 ) ⦙ اوامر الترحيب والردود ", data="gro"), Button.inline(" ( .م16 ) ⦙ اوامر الصيغ والجهات ", data="sejrz")],
    [Button.inline(" ( .م4 ) ⦙ حماية خاص والتلكراف ", data="grrz"), Button.inline(" ( .م15 ) ⦙ اوامر التسلية والميمز ", data="tslrzj")],
    [Button.inline(" ( .م12 ) ⦙ اوامر المساعدة والإذاعة ", data="r7brz"), Button.inline(" ( .م14 ) ⦙ اوامر المـلصقات وكوكل ", data="krrznd")],
    [Button.inline(" ( .م8 ) ⦙ اوامر التنظيف والتكرار ", data="jrzst"), Button.inline(" ( .م10 ) ⦙ اوامر الوقتي و التشغيل ", data="krrznd")],
    [Button.inline(" ( .م19 ) ⦙ اوامر اضافيه للسورس ", data="rfhrz"), Button.inline(" ( .م21 ) ⦙ اوامر تجميع النقاط وبوت وعد ", data="iiers")],
    [Button.inline(" ( .م5 ) ⦙ اوامر المنشن والانتحال ", data="uscuxrz")],  # زر واحد
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
        [Button.inline("التالي", data="jrzst"),
         Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(ROZADM, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"jrzst")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="tslrzj"),
         Button.inline("رجوع", data="l313l0")],
    ]
    await event.edit(GRTSTI, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"tslrzj")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="krrznd"),
         Button.inline("رجوع", data="jrzst")],
    ]
    await event.edit(JMAN, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"krrznd")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="rozbot"),
         Button.inline("رجوع", data="tslrzj")],
    ]
    await event.edit(TKPRZ, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rozbot")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="Jmrz"),
         Button.inline("رجوع", data="krrznd")],
    ]
    await event.edit(ROZBOT, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Jmrz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="r7brz"),
         Button.inline("رجوع", data="rozbot")],
    ]
    await event.edit(JROZT, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"r7brz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="sejrz"),
         Button.inline("رجوع", data="Jmrz")],
    ]
    await event.edit(JMTRD, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"sejrz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="gro"),
         Button.inline("رجوع", data="r7brz")],
    ]
    await event.edit(ROZSEG, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"gro")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="grrz"),
         Button.inline("رجوع", data="sejrz")],
    ]
    await event.edit(JMGR1, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"grrz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="iiers"),
         Button.inline("رجوع", data="gro")],
    ]
    await event.edit(ROZPRV, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"iiers")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="rfhrz"),
         Button.inline("رجوع", data="grrz")],
    ]
    await event.edit(HERP, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rfhrz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("التالي", data="uscuxrz"),
         Button.inline("رجوع", data="iiers")],
    ]
    await event.edit(T7SHIZ, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"uscuxrz")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("رجوع", data="l313l0")],
    ]
    await event.edit(CLORN, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"CLORN")))
@check_owner
async def _(event):
    # زر القائمة الرئيسية يعيدك للنص الأساسي مع زر التنقل
    buttons = [
    [Button.inline(" ( .م1 ) ⦙ اوامر الادمن ", data="l313l0")],  # زر واحد
    [Button.inline(" ( .م2 ) ⦙ اوامر المجموعة ", data="rozbot"), Button.inline(" ( .م18 ) ⦙ اوامر الحساب والترفيه ", data="Jmrz")],
    [Button.inline(" ( .م3 ) ⦙ اوامر الترحيب والردود ", data="gro"), Button.inline(" ( .م16 ) ⦙ اوامر الصيغ والجهات ", data="sejrz")],
    [Button.inline(" ( .م4 ) ⦙ حماية خاص والتلكراف ", data="grrz"), Button.inline(" ( .م15 ) ⦙ اوامر التسلية والميمز ", data="tslrzj")],
    [Button.inline(" ( .م12 ) ⦙ اوامر المساعدة والإذاعة ", data="r7brz"), Button.inline(" ( .م14 ) ⦙ اوامر المـلصقات وكوكل ", data="krrznd")],
    [Button.inline(" ( .م8 ) ⦙ اوامر التنظيف والتكرار ", data="jrzst"), Button.inline(" ( .م10 ) ⦙ اوامر الوقتي و التشغيل ", data="krrznd")],
    [Button.inline(" ( .م19 ) ⦙ اوامر اضافيه للسورس ", data="rfhrz"), Button.inline(" ( .م21 ) ⦙ اوامر تجميع النقاط وبوت وعد ", data="iiers")],
    [Button.inline(" ( .م5 ) ⦙ اوامر المنشن والانتحال ", data="uscuxrz")],  # زر واحد
]

    await event.edit(ROE, buttons=buttons)
