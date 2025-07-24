from JoKeRUB import l313l
from telethon import events
import requests
from collections import defaultdict

# ==== 1. أذكار الصباح والمساء ====
@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.(ادعية الصباح|ادعية المساء)"))
async def get_azkar(event):
    try:
        res = requests.get("https://alquran.vip/APIs/azkar")
        data = res.json()

        ztype = "الصباح" if "الصباح" in event.raw_text else "المساء"
        azkar_list = [z for z in data if z["category"] == f"أذكار {ztype}"]

        if not azkar_list:
            return await event.reply("❌ لم يتم العثور على الأذكار المطلوبة.")

        for z in azkar_list:
            text = f"📿 {z['zekr']}"
            if z.get("repeat"):
                text += f"\n🔁 التكرار: {z['repeat']}"
            if z.get("description"):
                text += f"\n📘 الشرح: {z['description']}"
            await event.reply(text)

    except Exception as e:
        await event.reply(f"⚠️ حدث خطأ أثناء جلب الأذكار:\n{e}")

# ==== 2. أدعية حسب التصنيف (قرآنية، نبوية، الأنبياء) ====
def filter_duaas(category_name, data):
    return [d for d in data if category_name in d.get("category", "")]

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.ادعية(?: (.+))?"))
async def categorized_duaas(event):
    try:
        category = event.pattern_match.group(1)
        res = requests.get("https://alquran.vip/APIs/دعاء")
        data = res.json()

        if not data:
            return await event.reply("❌ لم يتم العثور على أدعية.")

        if not category:
            return await event.reply(
                "**📚 التصنيفات المتوفرة:**\n"
                "- `.ادعية قرآنية`\n"
                "- `.ادعية نبوية`\n"
                "- `.ادعية الانبياء`\n\n"
                "✏️ استخدم أحد الأوامر أعلاه لعرض الأدعية."
            )

        category = category.strip().lower()
        title_map = {
            "قرآنية": "أدعية قرآنية",
            "نبوية": "أدعية نبوية",
            "الانبياء": "أدعية الأنبياء",
        }

        matched = title_map.get(category)
        if not matched:
            return await event.reply("❌ التصنيف غير معروف. جرب: قرآنية، نبوية، الانبياء")

        duaas = filter_duaas(matched, data)
        if not duaas:
            return await event.reply("❌ لا توجد أدعية تحت هذا التصنيف.")

        await event.reply(f"📚 {matched}:\n")

        for d in duaas:
            msg = f"📖 {d['text']}"
            if d.get("reference"):
                msg += f"\n📌 المرجع: {d['reference']}"
            await event.reply(msg)

    except Exception as e:
        await event.reply(f"⚠️ حدث خطأ:\n{e}")

# ==== 3. البحث عن سورة بالاسم ====
@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.سوره (.+)"))
async def surah_search(event):
    query = event.pattern_match.group(1).strip()
    url = "https://alquran.vip/APIs/surahs"

    try:
        res = requests.get(url)
        data = res.json()

        results = [s for s in data if query.lower() in s["name"].lower() or query == str(s["id"])]
        if not results:
            return await event.reply("❌ لم يتم العثور على سورة بهذا الاسم.")

        msg = "📖 نتائج البحث:\n\n"
        for s in results:
            msg += f"🕋 الاسم: {s['name']}\n"
            msg += f"🔢 رقم السورة: {s['id']}\n"
            msg += f"📍 عدد الآيات: {s['verses_count']}\n"
            msg += f"📖 مكان النزول: {s['place']}\n"
            msg += "ــــــــــــــــــــــــــــــــــــــــــــ\n"

        await event.reply(msg)
    except Exception as e:
        await event.reply(f"⚠️ خطأ أثناء جلب البيانات:\n{e}")

# ==== 4. جلب آيات سورة برقمها ====
@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.رقم السورة (\d{1,3})"))
async def ayah_by_number(event):
    surah_number = event.pattern_match.group(1).strip()
    url = f"https://alquran.vip/APIs/ayah?number={surah_number}"

    try:
        res = requests.get(url)
        data = res.json()

        if not isinstance(data, list) or len(data) == 0:
            return await event.reply("❌ لم يتم العثور على آيات لهذه السورة.")

        msg = f"📖 آيات السورة رقم {surah_number}:\n\n"
        for ayah in data:
            msg += f"{ayah['aya_number']}. {ayah['text']}\n"

        if len(msg) > 4000:
            for i in range(0, len(msg), 4000):
                await event.reply(msg[i:i+4000])
        else:
            await event.reply(msg)
    except Exception as e:
        await event.reply(f"⚠️ خطأ أثناء جلب الآيات:\n{e}")

# ==== 5. مواقيت الصلاة ====
async def fetch_prayer_times(event, country):
    url = f"https://alquran.vip/APIs/getPrayerTimes?country={country}"

    try:
        res = requests.get(url)
        data = res.json()

        if not data or "data" not in data:
            return await event.reply("❌ لم أتمكن من جلب مواقيت الصلاة لهذا البلد.")

        timings = data["data"]["timings"]
        date = data["data"]["date"]["gregorian"]["date"]

        msg = f"🕌 مواقيت الصلاة في {country} بتاريخ {date}:\n\n"
        for prayer, time in timings.items():
            msg += f"🕰️ {prayer}: {time}\n"

        await event.reply(msg)

    except Exception as e:
        await event.reply(f"⚠️ حدث خطأ أثناء جلب مواقيت الصلاة:\n{e}")

@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.(موعد الصلاة|صلاة) (.+)"))
async def prayer_times_handler(event):
    country = event.pattern_match.group(2).strip()
    await fetch_prayer_times(event, country)

# ==== 6. روابط صوتية للسور حسب قارئ ====
@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.صوت سوره (.+)"))
async def reciter_audio(event):
    reciter_name = event.pattern_match.group(1).strip()

    try:
        res = requests.get("https://alquran.vip/APIs/reciters")
        reciters = res.json()

        matched = [r for r in reciters if reciter_name.lower() in r.get("name", "").lower()]

        if not matched:
            return await event.reply("❌ لم أتمكن من العثور على قارئ بهذا الاسم.")

        reciter = matched[0]
        reciter_id = reciter.get("id")
        reciter_name_full = reciter.get("name")

        res_audio = requests.get(f"https://alquran.vip/APIs/reciterAudio?reciter_id={reciter_id}")
        audio_data = res_audio.json()

        if not audio_data:
            return await event.reply("❌ لا توجد روابط صوت لهذا القارئ.")

        msg = f"🎙️ روابط صوت السور للقارئ: {reciter_name_full}\n\n"
        for item in audio_data:
            surah_name = item.get("name")
            audio_url = item.get("audio_url")
            msg += f"▶️ {surah_name}: {audio_url}\n"

        if len(msg) > 4000:
            for i in range(0, len(msg), 4000):
                await event.reply(msg[i:i+4000])
        else:
            await event.reply(msg)

    except Exception as e:
        await event.reply(f"⚠️ حدث خطأ أثناء جلب روابط الصوت:\n{e}")

# ==== 7. أمر التوبه يعرض قائمة الأوامر ====
@l313l.on(events.NewMessage(outgoing=True, pattern=r"\.التوبه"))
async def show_commands(event):
    commands_list = """
📜 قائمة الأوامر المتوفرة:

.ادعية الصباح  
.ادعية المساء  
.ادعية  
.ادعية قرآنية  
.ادعية نبوية  
.ادعية الانبياء  
.سوره البقرة  
.رقم السورة 2  
.موعد الصلاة العراق  
.صلاة Egypt  
.صوت سوره ماهر المعيقلي  
"""
    await event.reply(commands_list)
