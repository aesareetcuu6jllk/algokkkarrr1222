import requests
from JoKeRUB import l313l  # حسب طلبك فقط استيراد

def get_instagram_info(text):
    if not text.startswith('.حساب انستا '):
        return None  # مش أمر انستا، تتجاهل
    
    username = text[len('.حساب انستا '):].strip()
    if not username:
        return "يرجى كتابة اسم المستخدم بعد الأمر."
    
    try:
        url = f"http://145.223.80.56:5091/instagram_info?username={username}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if 'error' in data:
            return f"خطأ: {data['error']}"
        
        result = (
            f"معلومات حساب انستا:\n"
            f"الاسم: {data.get('name', 'غير متوفر')}\n"
            f"المتابعين: {data.get('followers', 'غير متوفر')}\n"
            f"المتابَعون: {data.get('following', 'غير متوفر')}\n"
            f"عدد المنشورات: {data.get('posts', 'غير متوفر')}\n"
            f"الوصف: {data.get('bio', 'غير متوفر')}\n"
            f"https://instagram.com/{username}"
        )
        return result
    except Exception as e:
        return f"حدث خطأ أثناء جلب البيانات: {e}"
