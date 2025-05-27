import streamlit as st
from transformers import pipeline

# Ini HARUS di paling atas sebelum perintah Streamlit lainnya
st.set_page_config(page_title="Emotify", page_icon="🧠")

# Load model sekali saja
@st.cache_resource
def load_emotion_model():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

classifier = load_emotion_model()

# UI
st.title("🧠 Emotify")
st.markdown("Chatbot edukatif untuk meningkatkan literasi emosi remaja.")
st.markdown("Tulis perasaanmu hari ini, dan Emotify akan mengenali emosimu!\n")

# Input user
user_input = st.text_input("Bagikan perasaanmu di sini:")

if user_input:
    result = classifier(user_input)[0]
    emotion = result['label'].lower()
    confidence = round(result['score'] * 100, 2)

    # Tampilkan hasil deteksi emosi
    st.success(f"🤖 Emotify mengenali emosi kamu sebagai **{emotion}** (confidence: {confidence}%)")

    # Tambahkan respons edukatif
    responses = {
        "joy": "Senang mendengarnya! Tetap semangat dan terus sebarkan energi positif 😊",
        "sadness": "Tidak apa-apa merasa sedih. Kamu tidak sendiri. Yuk pelan-pelan atasi rasa ini 🌧️",
        "anger": "Marah itu wajar. Coba tarik napas pelan-pelan, kamu hebat sudah berusaha mengontrol emosi 🔥",
        "fear": "Takut adalah perasaan manusiawi. Yuk coba kenali sumbernya, kamu tidak harus hadapi semuanya sendirian 🤝",
        "surprise": "Wow, pasti hari ini terasa berbeda ya! Semoga jadi pengalaman yang berkesan 🎉",
        "disgust": "Rasa tidak nyaman itu valid. Mungkin sekarang saatnya rehat sejenak atau cari hal yang kamu suka 💆‍♀️"
    }

    # Tampilkan respons edukatif
    response = responses.get(emotion, "Terima kasih sudah berbagi. Emosi kamu valid dan penting untuk dikenali 🧠")
    st.info(f"💬 Emotify bilang: {response}")
