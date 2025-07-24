from JoKeRUB import l313l
import requests

@l313l.on_message  # أو حسب طريقة تعريف الأمر في مكتبتك
def insta_command(message):
    text = message.text
    if not text.startswith('.معلومات انستا '):
        return
    
    username = text[len('.معلومات انستا '):].strip()
    if not username:
        l313l.send_message(message.chat.id, "يرجى كتابة اسم المستخدم بعد الأمر.")
        return

    try:
        url = f"http://145.223.80.56:5091/instagram_info?username={username}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if 'error' in data:
            l313l.send_message(message.chat.id, f"خطأ: {data['error']}")
            return
        
        msg = (
            f"معلومات حساب انستا:\n"
            f"الاسم: {data.get('name', 'غير متوفر')}\n"
            f"المتابعين: {data.get('followers', 'غير متوفر')}\n"
            f"المتابَعون: {data.get('following', 'غير متوفر')}\n"
            f"عدد المنشورات: {data.get('posts', 'غير متوفر')}\n"
            f"الوصف: {data.get('bio', 'غير متوفر')}\n"
            f"https://instagram.com/{username}"
        )
        l313l.send_message(message.chat.id, msg)
    except Exception as e:
        l313l.send_message(message.chat.id, f"حدث خطأ أثناء جلب البيانات: {e}")
