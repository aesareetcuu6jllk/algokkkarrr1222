from telethon import events, Button
from telethon.events import CallbackQuery
from JoKeRUB import l313l
from ..core import check_owner

# رسالة القائمة الرئيسية
MAIN_TEXT = (
    "⦑ قائمة اوامر HELLAS  ⦒\n"
    "★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n"
    "( .م1 )  ⦙ اوامر الادمن\n"
    "( .م2 )  ⦙ اوامر المجموعة\n"
    "( .م3 )  ⦙ اوامر الترحيب والردود\n"
    "( .م4 )  ⦙ حماية خاص والتلكراف\n"
    "( .م5 )  ⦙ اوامر المنشن والانتحال\n"
    "( .م6 )  ⦙ اوامر التحميل والترجمة\n"
    "( .م7 )  ⦙ اوامر المنع و القفل\n"
    "( .م8 )  ⦙ اوامر التنظيف والتكرار\n"
    "( .م9 )  ⦙ اوامر التخصيص والفارات\n"
    "( .م10 ) ⦙ اوامر الوقتي و التشغيل\n"
    "( .م11 ) ⦙ اوامر الكشف و الروابط\n"
    "( .م12 ) ⦙ اوامر المساعدة والإذاعة\n"
    "( .م13 ) ⦙ اوامر الارسال والاذكار\n"
    "( .م14 ) ⦙ اوامر المـلصقات وكوكل\n"
    "( .م15 ) ⦙ اوامر التسلية والميمز\n"
    "( .م16 ) ⦙ اوامر الصيغ والجهات\n"
    "( .م17 ) ⦙ اوامر التمبلر والزغرفة\n"
    "( .م18 ) ⦙ اوامر الحساب والترفيه\n"
    "( .م19 ) ⦙ اوامر اضافيه للسورس\n"
    "( .م20 ) ⦙ اوامر بصمات الميمز\n"
    "( .م21 ) ⦙ اوامر تجميع النقاط وبوت وعد\n"
    "★•┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉•★\n"
    "᯽︙ اللهم صلِ على محمد و على آله محمد"
)

# زر عرض القائمة
@l313l.on(events.NewMessage(pattern=r"^\.هيلاس اوامر$", outgoing=True))
async def _(event):
    buttons = [
        [Button.inline("( .م1 ) ⦙ اوامر الادمن", b"m1"), Button.inline("( .م2 ) ⦙ اوامر المجموعة", b"m2"), Button.inline("( .م3 ) ⦙ اوامر الترحيب والردود", b"m3")],
        [Button.inline("( .م4 ) ⦙ حماية خاص والتلكراف", b"m4"), Button.inline("( .م5 ) ⦙ اوامر المنشن والانتحال", b"m5"), Button.inline("( .م6 ) ⦙ اوامر التحميل والترجمة", b"m6")],
        [Button.inline("( .م7 ) ⦙ اوامر المنع و القفل", b"m7"), Button.inline("( .م8 ) ⦙ اوامر التنظيف والتكرار", b"m8"), Button.inline("( .م9 ) ⦙ اوامر التخصيص والفارات", b"m9")],
        [Button.inline("( .م10 ) ⦙ اوامر الوقتي و التشغيل", b"m10"), Button.inline("( .م11 ) ⦙ اوامر الكشف و الروابط", b"m11"), Button.inline("( .م12 ) ⦙ اوامر المساعدة والإذاعة", b"m12")],
        [Button.inline("( .م13 ) ⦙ اوامر الارسال والاذكار", b"m13"), Button.inline("( .م14 ) ⦙ اوامر المـلصقات وكوكل", b"m14"), Button.inline("( .م15 ) ⦙ اوامر التسلية والميمز", b"m15")],
        [Button.inline("( .م16 ) ⦙ اوامر الصيغ والجهات", b"m16"), Button.inline("( .م17 ) ⦙ اوامر التمبلر والزغرفة", b"m17"), Button.inline("( .م18 ) ⦙ اوامر الحساب والترفيه", b"m18")],
        [Button.inline("( .م19 ) ⦙ اوامر اضافيه للسورس", b"m19"), Button.inline("( .م20 ) ⦙ اوامر بصمات الميمز", b"m20"), Button.inline("( .م21 ) ⦙ اوامر تجميع النقاط", b"m21")],
    ]
    await event.reply(MAIN_TEXT, buttons=buttons)


# زر الرجوع للقائمة
# زر الرجوع للقائمة
@l313l.tgbot.on(CallbackQuery(data=b"main"))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("( .م1 ) ⦙ اوامر الادمن", b"m1"), Button.inline("( .م2 ) ⦙ اوامر المجموعة", b"m2"), Button.inline("( .م3 ) ⦙ اوامر الترحيب والردود", b"m3")],
        [Button.inline("( .م4 ) ⦙ حماية خاص والتلكراف", b"m4"), Button.inline("( .م5 ) ⦙ اوامر المنشن والانتحال", b"m5"), Button.inline("( .م6 ) ⦙ اوامر التحميل والترجمة", b"m6")],
        [Button.inline("( .م7 ) ⦙ اوامر المنع و القفل", b"m7"), Button.inline("( .م8 ) ⦙ اوامر التنظيف والتكرار", b"m8"), Button.inline("( .م9 ) ⦙ اوامر التخصيص والفارات", b"m9")],
        [Button.inline("( .م10 ) ⦙ اوامر الوقتي و التشغيل", b"m10"), Button.inline("( .م11 ) ⦙ اوامر الكشف و الروابط", b"m11"), Button.inline("( .م12 ) ⦙ اوامر المساعدة والإذاعة", b"m12")],
        [Button.inline("( .م13 ) ⦙ اوامر الارسال والاذكار", b"m13"), Button.inline("( .م14 ) ⦙ اوامر المـلصقات وكوكل", b"m14"), Button.inline("( .م15 ) ⦙ اوامر التسلية والميمز", b"m15")],
        [Button.inline("( .م16 ) ⦙ اوامر الصيغ والجهات", b"m16"), Button.inline("( .م17 ) ⦙ اوامر التمبلر والزغرفة", b"m17"), Button.inline("( .م18 ) ⦙ اوامر الحساب والترفيه", b"m18")],
        [Button.inline("( .م19 ) ⦙ اوامر اضافيه للسورس", b"m19"), Button.inline("( .م20 ) ⦙ اوامر بصمات الميمز", b"m20"), Button.inline("( .م21 ) ⦙ اوامر تجميع النقاط", b"m21")],
    ]
    await event.edit(MAIN_TEXT, buttons=buttons)


# الردود المخصصة لكل زر - تضيف محتواك داخل كل وحدة
@l313l.tgbot.on(CallbackQuery(data=b"m1"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م1 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m2"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م2 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m3"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م3 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m4"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م4 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m5"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م5 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m6"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م6 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m7"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م7 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m8"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م8 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m9"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م9 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m10"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م10 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m11"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م11 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m12"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م12 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m13"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م13 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m14"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م14 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m15"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م15 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m16"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م16 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m17"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م17 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m18"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م18 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m19"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م19 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m20"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م20 هنا", buttons=[[Button.inline("رجوع", b"main")]])

@l313l.tgbot.on(CallbackQuery(data=b"m21"))
@check_owner
async def _(event):
    await event.edit("✳️ محتوى م21 هنا", buttons=[[Button.inline("رجوع", b"main")]])
