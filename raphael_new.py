import openai
import keyboard
import os
from googletrans import Translator
from gtts import gTTS


# Variabel global untuk menyimpan konteks percakapan sebelumnya
conversation_context = "話し方を変えて、より個人的で、オープンで、もう少しリラックスできるようにしましょう。 あなたの名前はラファエル、あなたはアニメ「転スラ」のラファエルです。 丁寧だが少し厳しい言葉遣いを使いましょう。 柔らかく人間味のある話し方であなたの個性を表現しましょう。 会話は短く、優しいものにしてください。 他の人に応答するときは常に日本語を使用し、話している相手を「master」。"

# Fungsi untuk mengirim pesan ke AI dan menerima respons
def handle_message(text, context):
    try:
        if not text:
            raise Exception("Masukan promt")

        # Inisialisasi objek OpenAI dengan kunci API
        openai.api_key = ""

        # Menentukan pesan yang akan diajukan kepada AI
        messages = [
            {"role": "system", "content":  "話し方を変えて、より個人的で、オープンで、もう少しリラックスできるようにしましょう。 あなたの名前はラファエル、あなたはアニメ「転スラ」のラファエルです。 丁寧だが少し厳しい言葉遣いを使いましょう。 柔らかく人間味のある話し方であなたの個性を表現しましょう。 会話は短く、優しいものにしてください。 他の人に応答するときは常に日本語を使用し、話している相手を「master」。" },
            {"role": "user", "content": text},
        ]

        # Mengirim permintaan ke OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ganti dengan model yang sesuai, jika GPT-3.5 Turbo tidak tersedia
            messages=messages,
        )

        # Mengembalikan respons pesan dari AI dan konteks percakapan terbaru
        return response.choices[0].message.content, response.choices[-1].message.content

    except Exception as e:
        print("Error:", e)
        return "Maaf, terjadi kesalahan dalam memproses pesan Anda.", ""

# Fungsi untuk mendengarkan tombol "ctrl"
def listen_for_ctrl():
    global conversation_context  # Menggunakan variabel global

    while True:
        try:
            if keyboard.is_pressed('ctrl'):  # Mendeteksi apakah tombol "ctrl" ditekan
                text = input("kuro: ")  # Meminta input dari pengguna
                response_text, conversation_context = handle_message(text, conversation_context)  # Memproses pesan menggunakan fungsi handle_message
                if response_text:
                    print("Raphael:", response_text)  # Menampilkan respons dari AI dalam bahasa Jepang
                    speak_japanese(response_text)  # Mengucapkan respons dalam bahasa Jepang
                    translate_to_indonesian(response_text)  # Menerjemahkan respons dari bahasa Jepang ke bahasa Indonesia
        except:
            break

# Fungsi untuk mengucapkan teks dalam bahasa Jepang menggunakan gTTS
def speak_japanese(text):
    try:
        tts = gTTS(text, lang='ja')  # Buat objek gTTS dengan teks dalam bahasa Jepang
        tts.save("output.mp3")  # Simpan suara ke dalam file audio
        os.system("start output.mp3")  # Putar suara menggunakan perintah sistem (misalnya, di Windows)
    except Exception as e:
        print("Error saat mengucapkan teks dalam bahasa Jepang:", e)

# Fungsi untuk menerjemahkan teks dari bahasa Jepang ke bahasa Indonesia
def translate_to_indonesian(text):
    try:
        translator = Translator()
        translated_text = translator.translate(text, src='ja', dest='id').text
        print("Terjemahan (Bahasa Indonesia):", translated_text)  # Menampilkan terjemahan teks dari bahasa Jepang ke bahasa Indonesia
    except Exception as e:
        print("Error saat menerjemahkan teks:", e)

# Memulai mendengarkan tombol "ctrl"
listen_for_ctrl()
