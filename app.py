import streamlit as st
from transformers import pipeline

# Ini HARUS di paling atas
st.set_page_config(page_title="Emotify", page_icon="🧠")

@st.cache_resource
def load_emotion_model():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

classifier = load_emotion_model()

st.title("🧠 Emotify")
st.markdown("Chatbot edukatif untuk meningkatkan literasi emosi remaja.")
st.markdown("Tulis perasaanmu hari ini, dan Emotify akan mengenali emosimu!\n")

user_input = st.text_input("Bagikan perasaanmu di sini:")

if user_input:
    output = classifier(user_input)

    if output and isinstance(output, list) and isinstance(output[0], list) and len(output[0]) > 0:
        result = output[0][0]  # akses dict di dalam list
        emotion = result['label'].lower()
        confidence = round(result['score'] * 100, 2)

        st.success(f"🤖 Emotify mengenali emosi kamu sebagai **{emotion}** (confidence: {confidence}%)")

        responses = {
            "joy": "Senang mendengarnya! Tetap semangat dan terus sebarkan energi positif 😊",
            "sadness": "Tidak apa-apa merasa sedih. Kamu tidak sendiri. Yuk pelan-pelan atasi rasa ini 🌧️",
            "anger": "Marah itu wajar. Coba tarik napas pelan-pelan, kamu hebat sudah berusaha mengontrol emosi 🔥",
            "fear": "Takut adalah perasaan manusiawi. Yuk coba kenali sumbernya, kamu tidak harus hadapi semuanya sendirian 🤝",
            "surprise": "Wow, pasti hari ini terasa berbeda ya! Semoga jadi pengalaman yang berkesan 🎉",
            "disgust": "Rasa tidak nyaman itu valid. Mungkin sekarang saatnya rehat sejenak atau cari hal yang kamu suka 💆‍♀️"
        }

        response = responses.get(emotion, "Terima kasih sudah berbagi. Emosi kamu valid dan penting untuk dikenali 🧠")
        st.info(f"💬 Emotify bilang: {response}")
    else:
        st.error("Maaf, Emotify tidak bisa mengenali emosi dari teks tersebut.")
