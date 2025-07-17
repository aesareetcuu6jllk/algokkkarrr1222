from JoKeRUB import l313l
import requests
import base64
from telebot import types

class ImageConverter:
    def convert_image_to_base64(self, file_data):
        return base64.b64encode(file_data).decode('utf-8')

    def call_google_vision_api(self, encoded_image):
        headers = {
            'User-Agent': 'Google-API-Java-Client Google-HTTP-Java-Client/1.43.3 (gzip)',
            'x-android-package': 'image.to.text.ocr',
            'x-android-cert': 'ad32d34755bb3b369a2ea8dfe9e0c385d73f80f0',
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'vision.googleapis.com',
            'Connection': 'Keep-Alive'
        }
        params = {'key': 'AIzaSyA5MInkpSbdSbmozCQSuBY3pylSTgmLlaM'}
        json_data = {
            'requests': [{
                'features': [{'maxResults': 10, 'type': 'TEXT_DETECTION'}],
                'image': {'content': encoded_image}
            }]
        }
        response = requests.post(
            'https://vision.googleapis.com/v1/images:annotate',
            params=params,
            headers=headers,
            json=json_data
        )
        return response.json() if response.status_code == 200 else "Error: " + response.text


@l313l.bot.message_handler(func=lambda m: m.text and m.text.startswith('.اقرء'))
def handle_ocr_command(message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        l313l.bot.reply_to(message, "يجب الرد على صورة بالأمر `.اقرء`.")
        return

    wait = l313l.bot.send_message(message.chat.id, "• جاري قراءة النص من الصورة ...")

    try:
        file_info = l313l.bot.get_file(message.reply_to_message.photo[-1].file_id)
        downloaded_file = l313l.bot.download_file(file_info.file_path)

        converter = ImageConverter()
        encoded_image = converter.convert_image_to_base64(downloaded_file)
        vision_response = converter.call_google_vision_api(encoded_image)

        l313l.bot.delete_message(message.chat.id, wait.id)

        if 'responses' in vision_response and vision_response['responses']:
            texts = [t['description'] for t in vision_response['responses'][0].get('textAnnotations', [])]
            if texts:
                extracted_text = texts[0]
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton("نسخ النص", callback_data="copy_text"))
                l313l.bot.send_message(message.chat.id, f"📄 النص المستخرج:\n\n```{extracted_text}```", parse_mode="Markdown", reply_markup=markup)
            else:
                l313l.bot.send_message(message.chat.id, "❌ لم يتم العثور على نص في الصورة.")
        else:
            l313l.bot.send_message(message.chat.id, f"❌ فشل في الاتصال بـ API: {vision_response}")
    except Exception as e:
        l313l.bot.delete_message(message.chat.id, wait.id)
        l313l.bot.send_message(message.chat.id, f"⚠️ حدث خطأ أثناء المعالجة:\n{e}")


@l313l.bot.callback_query_handler(func=lambda call: call.data == "copy_text")
def handle_copy_text(call):
    l313l.bot.answer_callback_query(call.id, "✅ تم نسخ النص.")
