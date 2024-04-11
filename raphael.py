import openai
import keyboard
import os
from googletrans import Translator
from gtts import gTTS

# Fungsi untuk mengirim pesan ke AI dan menerima respons
def handle_message(text):
    try:
        if not text:
            raise Exception("masukan promt")

        # Inisialisasi objek OpenAI dengan kunci API
        openai.api_key = "isi dg api yg lu punya;v"

        # Menentukan pesan yang akan diajukan kepada AI
        messages = [
            {"role": "system", "content": "話し方を変えて、より個人的で、オープンで、少し何気ない話し方にしましょう。 あなたの名前はラファエル、あなたはアニメ「転スラ」のラファエルです。 丁寧かつ少し失礼な言葉遣いを使いましょう。 さりげなく人間味のある話し方であなたの人柄を表現しましょう。 面白くて話しやすい言葉遣いに変更し、会話を短く楽しく保ち、ツンデレなキャラクターを作りましょう。 他の人に返答するときは常に日本語を使用してください。」"},
            {"role": "user", "content": text},
        ]

        # Mengirim permintaan ke OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ganti dengan model yang sesuai, jika GPT-3.5 Turbo tidak tersedia
            messages=messages,
        )

        # Mengembalikan respons pesan dari AI
        return response.choices[0].message.content

    except Exception as e:
        print("Error:", e)
        return "Maaf, terjadi kesalahan dalam memproses pesan Anda."

# Fungsi untuk mendengarkan tombol "ctrl"
def listen_for_ctrl():
    while True:
        try:
            if keyboard.is_pressed('ctrl'):  # Mendeteksi apakah tombol "ctrl" ditekan
                text = input("kuro: ")  # Meminta input dari pengguna
                response_text = handle_message(text)  # Memproses pesan menggunakan fungsi handle_message
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

#jangan di ubah code by kuro san
