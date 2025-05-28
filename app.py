import streamlit as st
from transformers import pipeline

# Konfigurasi halaman
st.set_page_config(page_title="Emotify", page_icon="🧠")

# Muat model
@st.cache_resource
def load_emotion_model():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

classifier = load_emotion_model()

# Tampilan utama
st.title("🧠 Emotify")
st.markdown("Chatbot edukatif untuk meningkatkan literasi emosi remaja.")
st.markdown("Tulis perasaanmu hari ini, dan Emotify akan mengenali emosimu!\n")

user_input = st.text_input("Bagikan perasaanmu di sini:")

if user_input:
    output = classifier(user_input)

    try:
        result = output[0][0]  # ✅ Perbaikan utama: dua kali indeks
        emotion = result["label"].lower()
        confidence = round(result["score"] * 100, 2)

        st.success(f"🤖 Emotify mengenali emosi kamu sebagai **{emotion}** (confidence: {confidence}%)")

        responses = {
            "joy": "Senang mendengarnya! Tetap semangat dan terus sebarkan energi positif 😊",
            "sadness": "Tidak apa-apa merasa sedih. Kamu tidak sendiri. Yuk pelan-pelan atasi rasa ini 🌧️",
            "anger": "Marah itu wajar. Coba tarik napas pelan-pelan, kamu hebat sudah berusaha mengontrol emosi 🔥",
            "fear": "Takut adalah perasaan manusiawi. Yuk coba kenali sumbernya, kamu tidak harus hadapi semuanya sendirian 🤝",
            "surprise": "Wow, pasti hari ini terasa berbeda ya! Semoga jadi pengalaman yang berkesan 🎉",
            "disgust": "Rasa tidak nyaman itu valid. Mungkin sekarang saatnya rehat sejenak atau cari hal yang kamu suka 💆‍♀️",
            "neutral": "Emosimu tampak netral. Kalau ada yang sedang mengganggu pikiran, tak apa untuk menceritakannya ✨"
        }

        # Respons berdasarkan keyword (fallback)
        keywords = {
            "benci": "Kamu sedang merasa sangat terganggu ya. Coba cerita ke orang yang kamu percaya, itu bisa membantu 🫂",
            "capek": "Istirahat sejenak itu penting. Jangan lupa sayangi dirimu sendiri 💆",
            "sendiri": "Merasa sendiri itu berat. Tapi kamu tidak sendirian. Coba hubungi sahabat atau keluarga 🤗",
            "bingung": "Bingung itu wajar. Coba uraikan satu per satu. Kamu pasti bisa pelan-pelan ✨",
            "kesepian": "Rasa sepi kadang datang diam-diam. Cari ruang nyaman dan hangatkan hatimu dengan hal-hal kecil 💖"
        }

        response = responses.get(emotion)
        if not response:
            for key, msg in keywords.items():
                if key in user_input.lower():
                    response = msg
                    break
        if not response:
            response = "Terima kasih sudah berbagi. Emosi kamu valid dan penting untuk dikenali 🧠"

        st.info(f"💬 Emotify bilang: {response}")
    except Exception as e:
        st.error(f"Ada kesalahan saat mengenali emosi: {e}")
