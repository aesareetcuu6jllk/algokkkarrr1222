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
t1 = """ ** قائمة اوامر الارسال **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.امر الصورة الذاتية` )\n- ( `.اوامر التحذيرات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` ) \n- ( `.اوامر الاذكار` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
t2 = """⦑ قائمة أوامر البصمات 🎧 ⦒\n"
        "★•────────────•★\n"
        "`.بصمات1`\n"
        "`.بصمات2`\n"
        "`.بصمات3`\n"
        "`.بصمات4`\n"
        "`.بصمات5`\n"
        "`.بصمات6`\n"
        "`.بصمات7`\n"
        "`.بصمات8`\n"
        "`.بصمات9`\n"
        "`.بصمات10`\n"
        "`.بصمات11`\n"
        "`.بصمات12`\n"
        "★•────────────•★\n"
        "CH : @HELLASUserBot"""
t3 = """قائمة اوامر الحساب والقنوات والمجموعات التي تديرها\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★➖\n᯽︙ اختر احدى هذه الاوامر\n\n- ( `.معلوماتي` ) \n( `.قائمه قنواتي` ) \n( `.قائمه كروباتي` )\n\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★➖\n⌔︙CH : @HELLASUserBot"""
t4 = """قائمة اوامر التجميع\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★➖\n᯽︙ اختر احدى هذه الاوامر\n\n- ( `.تجميع المليار` )\n- ( `.تجميع HELLAS ` )\n- ( `.تجميع ارشقلي` )\n- ( `.تجميع ارشقلي` )\n\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★➖\n⌔︙CH : @HELLASUserBot"""
t5 = """ شـرح عـن اوامـر تـحويل الصـيغ :\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه الاوامر\n\n- ( `.تحويل صورة` )\n بالرد على الملصق لتحويله الى صورة\n\n- ( `.تحويل ملصق` )\n بالرد على الصورة لتحويلها الى الملصق\n\n- ( `.تحويل voice` )\nبالرد على مقطع اغنية لتحويله على شكل بصمة صوتية\n\n- ( `.تحويل mp3` )\nبالرد على البصمة الصوتية لتحويلها على شكل  مقطع mp3\n\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n᯽︙ CH : @HELLASUserBot"""
t6 = """قائمة اوامر التحشيش :\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★➖\n ᯽︙ اختر احدى هذه القوائم\n\n**جميع اوامـر التحشيش تستخـدم بالـرد عـلى الشخص**\n\n- ( `.رفع تاج` )\n- ( `.رفع بكلبي` )\n- ( `.رفع مطي` )\n- ( `.رفع جلب` ) \n- ( `.رفع قرد` )\n- ( `.رفع مرتي` )\n- ( `.رفع زوجي` )\n- ( `.نسبة الانوثة` )\n- ( `.نسبة الحب` )\n- ( `.نسبة الغباء` ) \n- ( `.رفع زاحف` ) \n- ( `.رفع كحبة` ) \n- ( `.رفع فرخ` ) \n- ( `.رزله` ) \n- ( `.رفع صاك` ) \n- ( `.رفع حاته` ) \n- ( `.رفع بقره` ) \n- ( `.رفع ايجة` )\n- ( `.رفع زبال` )\n- ( `.رفع كواد` )\n- ( `.رفع ديوث` )\n- ( `.رفع مجنب` )\n- ( `.رفع مميز` )\n- ( `.رفع ادمن` )\n- ( `.رفع منشئ` )\n- ( `.رفع مالك` )\n- ( `.رفع وصخ` )\n- ( `.نسبة الكذب` )\n- ( `.نسبة الدياثه` )\n- ( `.نسبة الشذوذ` )\n- ( `.نسبة الجمال` )\n- ( `.نسبة الخيانه` )\n\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★➖\n⌔︙CH : @HELLASUserBot """
t7 = """شرح امر الصورة الذاتية :\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★➖\n᯽︙ اختر احدى هذه الاوامر\n\n- ( `.ذاتية` )\n بالـرد عـلى الصـورة ذاتيـة الـتدمير ليـقوم بـحفظها وارسالـها لك فـي الرسائل الـمحفوظة بسرية وبـدون عـلم الـطرف الأخر \n- ( `.حفظ` )\n بالـرد عـلى الصـورة الموجوده في المجموعة ذات التقييد المحتوى ليـقوم بـحفظها وارسالـها لك فـي الرسائل الـمحفوظة بسرية وبـدون عـلم الـطرف الأخر\n( `.الذاتية تشغيل` )\n قم بكتابة الامر في أي مكان ليقوم بتفعيل الامر وحفظ الصور الذاتية التدمير تلقائياً\n( `.الذاتية تعطيل` )\n قم بكتابة الامر في مكان لتقوم بتعطيل الامر الصورة الذاتية التدمير\n\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★➖\n⌔︙CH : @HELLASUserBot """
t8 = """**📢 أوامر النشر التلقائي:**\n\n"
        "🔹 **الأوامر المحددة (تحتاج الرد على رسالة):**\n"
        "▪️ `.نشر_كروبات 60`\n"
        "↳ نشر الرسالة التي ترد عليها في كل الكروبات كل 60 ثانية.\n\n"
        "▪️ `.نشر_عدد 60 5`\n"
        "↳ نشر الرسالة التي ترد عليها في أول 5 كروبات كل 60 ثانية.\n\n"
        "🔹 **الأوامر غير المحددة (تنفذ مباشرة):**\n"
        "▪️ `.ايقاف_نشر_كروبات`\n"
        "↳ إيقاف النشر المستمر في كل الكروبات.\n\n"
        "▪️ `.ايقاف_نشر_عدد`\n"
        "↳ إيقاف النشر المحدود.\n\n"
        "🔹 **أمر التكرار (يعمل فقط في المجموعات):**\n"
        "▪️ `.مكرر 300 10000`\n"
        "↳ تكرار الرسالة التي ترد عليها 10000 مرة، كل 300 ثانية بين كل تكرار.\n\n"
        "🔹 **أوامر مساعدة:**\n"
        "▪️ `.ايقاف التكرار`\n"
        "↳ إيقاف عملية التكرار المستمرة.\n\n"
        "▪️ `.فحص النشر`\n"
        "↳ يعرض حالة كل عمليات النشر الجارية.\n\n"
        "▪️ `.حالتي`\n"
        "↳ فحص إذا كنت محظور من @SpamBot.\n\n"
        "🔹 **تعليمات هامة:**\n"
        "• قم بالرد على الرسالة التي تريد نشرها قبل استخدام أوامر النشر المحددة.\n"
        "• الأوامر الخاصة بالإيقاف تعمل فورًا بدون الحاجة لرد.\n"
        "• تأكد من أن البوت يعمل وله صلاحيات النشر في الكروبات المستهدفة.\n"""

t9 = """** 🚀 قائمة أنواع اليوزرات المتاحة للصيد 🚀 **\n\n"
    
    "• **اليوزرات الثلاثية:**\n"
    "➤ `.صيد ثلاثي1` - **مثال:** H_R_B\n"
    "➤ `.صيد ثلاثي2` - **مثال:** H_4_B\n"
    "➤ `.صيد ثلاثي3` - **مثال:** H_4_0\n\n"
    
    "• **اليوزرات الرباعية:**\n"
    "➤ `.صيد رباعي1` - **مثال:** HHH_B\n"
    "➤ `.صيد رباعي2` - **مثال:** H_BBB\n"
    "➤ `.صيد رباعي3` - **مثال:** HH_BB\n"
    "➤ `.صيد رباعي4` - **مثال:** HH_HB\n"
    "➤ `.صيد رباعي5` - **مثال:** HH_BH\n"
    "➤ `.صيد رباعي6` - **مثال:** HB_BH\n"
    "➤ `.صيد رباعي7` - **مثال:** HB_HB\n"
    "➤ `.صيد رباعي8` - **مثال:** HB_BB\n\n"
    
    "• **اليوزرات شبه الرباعية:**\n"
    "➤ `.صيد شبه رباعي1` - **مثال:** H_H_H_B\n"
    "➤ `.صيد شبه رباعي2` - **مثال:** H_B_B_B\n"
    "➤ `.صيد شبه رباعي3` - **مثال:** H_BB_H\n"
    "➤ `.صيد شبه رباعي4` - **مثال:** H_BB_B\n\n"
    
    "• **اليوزرات الخماسية:**\n"
    "➤ `.صيد خماسي حرفين1` - **مثال:** HHHBR\n"
    "➤ `.صيد خماسي حرفين2` - **مثال:** H4BBB\n"
    "➤ `.صيد خماسي ارقام` - **مثال:** HB444\n"
    "➤ `.صيد خماسي حرفين3` - **مثال:** HBBBR\n\n"
    
    "• **اليوزرات السداسية:**\n"
    "➤ `.صيد سداسي_حرفين1` - **مثال:** HBHHHB\n"
    "➤ `.صيد سداسي_حرفين2` - **مثال:** HHHHBB\n"
    "➤ `.صيد سداسي_حرفين3` - **مثال:** HHHBBH\n"
    "➤ `.صيد سداسي_حرفين4` - **مثال:** HHBBHH\n"
    "➤ `.صيد سداسي_حرفين5` - **مثال:** HBBHHH\n"
    "➤ `.صيد سداسي_حرفين6` - **مثال:** HHBBBB\n"
    "➤ `.صيد سداسي_شرطه` - **مثال:** HHHH_B\n\n"
    
    "• **اليوزرات السباعية:**\n"
    "➤ `.صيد سباعيات1` - **مثال:** HHHHHHB\n"
    "➤ `.صيد سباعيات2` - **مثال:** HHHHHBH\n"
    "➤ `.صيد سباعيات3` - **مثال:** HHHHBHH\n"
    "➤ `.صيد سباعيات4` - **مثال:** HHHBHHH\n"
    "➤ `.صيد سباعيات5` - **مثال:** HHBHHHH\n"
    "➤ `.صيد سباعيات6` - **مثال:** HBHHHHH\n"
    "➤ `.صيد سباعيات7` - **مثال:** HBBBBBB\n\n"
    
    "• **يوزرات البوتات:**\n"
    "➤ `.صيد بوتات1` - **مثال:** HB_Bot\n"
    "➤ `.صيد بوتات2` - **مثال:** H_BBot\n"
    "➤ `.صيد بوتات3` - **مثال:** HB4Bot\n"
    "➤ `.صيد بوتات4` - **مثال:** H4BBot\n"
    "➤ `.صيد بوتات5` - **مثال:** H44Bot\n"
    "➤ `.صيد بوتات6` - **مثال:** HRBBot\n"
    "➤ `.صيد بوتات7` - **مثال:** HHBBot - HH4Bot\n"
    "➤ `.صيد بوتات8` - **مثال:** HHBBot\n"
    "➤ `.صيد بوتات9` - **مثال:** HH4Bot\n\n"
    
    "🛠 **هذه اوامر سورس 𝐇𝐞𝐥𝐥𝐚𝐬 لصيد اليوزرات لإظهار أوامر الصيد والتثبيت الأساسية:**\n"
    "➤ استخدم الأمر: `.الصيد` أو `.التثبيت`"""

t10 = """• اوامـر الصيـد والتثبيت هيلاس سورس • \n\n"
    "•╎ أولاً: قائمة أوامر تشيكـر صيد معرفات تيليجرام:\n"
    "- **`.النوع`**\n"
    "  ⪼ لعرض الأنواع التي يمكن صيدها مع الأمثلة.\n"
    "- **`.صيد` + النوع**\n"
    "  ⪼ لصيد يوزرات عشوائية حسب النوع المحدد.\n"
    "- **`.حالة الصيد`**\n"
    "  ⪼ لمعرفة حالة تقدم عملية الصيد.\n"
    "- **`.صيد ايقاف`**\n"
    "  ⪼ لإيقاف عملية الصيد الحالية.\n\n"
    "•╎ ثانياً: قائمة أوامر تشيكـر تثبيت معرفات تيليجرام:\n"
    "- **`.تثبيت_قناة` + اليوزر**\n"
    "  ⪼ لتثبيت اليوزر بقناة معينة إذا أصبح متاحًا.\n"
    "- **`.تثبيت_حساب` + اليوزر**\n"
    "  ⪼ لتثبيت اليوزر بحسابك مباشرة إذا أصبح متاحًا.\n"
    "- **`.تثبيت_بوت` + اليوزر**\n"
    "  ⪼ لتثبيت اليوزر في بوت فاذر إذا أصبح متاحًا.\n\n"
    "•╎ اوامر حالة التثبيت :\n"
    "- **`.حالة تثبيت_القناة`**\n"
    "  ⪼ لمعرفة حالة تقدم التثبيت التلقائي على القناة.\n"
    "- **`.حالة تثبيت_الحساب`**\n"
    "  ⪼ لمعرفة حالة تقدم التثبيت التلقائي على حسابك.\n"
    "- **`.حالة تثبيت_البوت`**\n"
    "  ⪼ لمعرفة حالة تقدم التثبيت التلقائي على بوت فاذر.\n\n"
    "•╎ اوامر أيقاف التثبيت :\n"
    "- **`.ايقاف تثبيت_القناة`**\n"
    "  ⪼ لإيقاف عملية تثبيت القناة التلقائي.\n"
    "- **`.ايقاف تثبيت_الحساب`**\n"
    "  ⪼ لإيقاف عملية تثبيت الحساب التلقائي.\n"
    "- **`.ايقاف تثبيت_البوت`**\n"
    "  ⪼ لإيقاف عملية تثبيت البوت التلقائي.\n\n"
    "🚨 ملاحظات مهمة قبل استخدام أوامر الصيد والتثبيت:\n"
    "- تأكد من مساحه القنوات حتا اذا مقبطه وصاد يوزر وين يخليه اذا انت مخليه كله قنوات ف فرغ قنوات وتأكد اكو مساحه.\n"
    "- لاتوقف الصيد حتا لو طول تمام!!.\n"
    "- الصبر جميل ويا سورس 𝐇𝐞𝐥𝐥𝐚𝐬 : @HELLASUserBot.\n"""

t11 = """🎭 هاذي هيه بصمات ميمز سورس هيلاس:

`هاروني`
`همبركر`
`لا شماته`
`تفضل`
`اشكرج طبعا`
`ماردنا الطلايب`
`موال سلام`
`اف مبروك`
`الاكننا الافضل`
`اطلع بره`
`بليز ترامب`
`واجب`
`حيدر كيمز`
`شماته`
`يلا دي`
`وين كلاوات`
`لكيتني`
`يعني يعني`
`يبو فاضل`
`جلاب`
`حسناء`
`انت اسكت`
`اسكت ياخي`
`ارسلني حمزه`
`عفطه`
`حيل ضايج`
`شجاي تلغي`
`كافي جلبت`
`هاي شبيك`
`انا اسفف`
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

    if query.startswith("اوامري") and event.query.user_id == bot.uid:
        buttons = [
            [Button.inline("🔐 اوامر الادمن", data="l313l0")],
            [Button.inline("👥 اوامر المجموعة", data="rozbot"), Button.inline("🎭 الحساب والترفيه", data="Jmrz")],
            [Button.inline("💬 الترحيب والردود", data="gro"), Button.inline("📇 الصيغ والجهات", data="sejrz")],
            [Button.inline("🔒 حماية خاص وتلكراف", data="grrz"), Button.inline("🎮 التسلية والميمز", data="tslrzj")],
            [Button.inline("📢 المساعدة والإذاعة", data="r7brz"), Button.inline("🎓 الملصقات وكوكل", data="krrznd1")],
            [Button.inline("🧹 التنظيف والتكرار", data="jrzst"), Button.inline("🕒 الوقتي والتشغيل", data="krrznd")],
            [Button.inline("📤 الارسال والاذكار", data="t1"), Button.inline("🎼 بصمات بنات", data="t2")],
            [Button.inline("👤 معلومات حسابي", data="t3"), Button.inline("🪙 تجميع النقاط", data="t4")],
            [Button.inline("🖼️ الصور الذاتية", data="t7")],
            [Button.inline("📣 النشر التلقائي", data="t8")],
	    [Button.inline("بصمات الميمز", data="t11")],
            [Button.inline("🔁 تحويل الصيغ", data="t5"), Button.inline("😂 اوامر التحشيش", data="t6")],
            [Button.inline("🎯 صيد يوزرات", data="t9"), Button.inline("📌 تثبيت يوزرات", data="t10")],
            [Button.inline("🧩 اوامر إضافية للسورس", data="rfhrz"), Button.inline("🤖 تجميع النقاط + بوت وعد", data="iiers")],
            [Button.inline("👥 المنشن والانتحال", data="uscuxrz")]
        ]

        if JEP_IC and JEP_IC.endswith((".jpg", ".png", "gif", "mp4")):
            result = builder.photo(
                JEP_IC,
                text=ROE,
                buttons=buttons,
                link_preview=False
            )
        elif JEP_IC:
            result = builder.document(
                JEP_IC,
                title="JoKeRUB",
                text=ROE,
                buttons=buttons,
                link_preview=False
            )
        else:
            result = builder.article(
                title="JoKeRUB",
                text=ROE,
                buttons=buttons,
                link_preview=False
            )

        await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="اوامري"))
async def repo(event):
    if event.fwd_from:
        return
    F_O_1 = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(F_O_1, "اوامري")
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

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"t1")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(t1, buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"t11")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(t11, buttons=buttons)
	
@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"t2")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(t2, buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"t3")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(t3, buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"t4")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(t4, buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"t5")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(t5, buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"t6")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(t6, buttons=buttons)



@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"t7")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(t7, buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"t8")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(t8, buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"t9")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(t9, buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"t10")))
@check_owner
async def _(event):
    buttons = [
        [Button.inline("القائمة الرئيسية", data="CLORN")],
    ]
    await event.edit(t10, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"CLORN")))
@check_owner
async def _(event):
    # زر القائمة الرئيسية يعيدك للنص الأساسي مع زر التنقل
    buttons = [
            [Button.inline("🔐 اوامر الادمن", data="l313l0")],
            [Button.inline("👥 اوامر المجموعة", data="rozbot"), Button.inline("🎭 الحساب والترفيه", data="Jmrz")],
            [Button.inline("💬 الترحيب والردود", data="gro"), Button.inline("📇 الصيغ والجهات", data="sejrz")],
            [Button.inline("🔒 حماية خاص وتلكراف", data="grrz"), Button.inline("🎮 التسلية والميمز", data="tslrzj")],
            [Button.inline("📢 المساعدة والإذاعة", data="r7brz"), Button.inline("🎓 الملصقات وكوكل", data="krrznd1")],
            [Button.inline("🧹 التنظيف والتكرار", data="jrzst"), Button.inline("🕒 الوقتي والتشغيل", data="krrznd")],
            [Button.inline("📤 الارسال والاذكار", data="t1"), Button.inline("🎼 بصمات بنات", data="t2")],
            [Button.inline("👤 معلومات حسابي", data="t3"), Button.inline("🪙 تجميع النقاط", data="t4")],
            [Button.inline("🖼️ الصور الذاتية", data="t7")],
            [Button.inline("📣 النشر التلقائي", data="t8")],
	    [Button.inline("بصمات الميمز", data="t11")],
            [Button.inline("🔁 تحويل الصيغ", data="t5"), Button.inline("😂 اوامر التحشيش", data="t6")],
            [Button.inline("🎯 صيد يوزرات", data="t9"), Button.inline("📌 تثبيت يوزرات", data="t10")],
            [Button.inline("🧩 اوامر إضافية للسورس", data="rfhrz"), Button.inline("🤖 تجميع النقاط + بوت وعد", data="iiers")],
            [Button.inline("👥 المنشن والانتحال", data="uscuxrz")]
        ]

    await event.edit(ROE, buttons=buttons)
