import streamlit as st
import random
import time

# 🎨 Set page config for a professional look
st.set_page_config(page_title="Quiz App", page_icon="📝", layout="centered")

# 🎯 Title with Emoji
st.title("📝 Interactive Quiz Challenge")

# 📌 Questions List
questions = [
    {"question": "🇵🇰 What is the capital of Pakistan?", "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], "answer": "Islamabad"},
    {"question": "👤 Who is the founder of Pakistan?", "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"], "answer": "Muhammad Ali Jinnah"},
    {"question": "🗣️ Which is the national language of Pakistan?", "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"], "answer": "Urdu"},
    {"question": "💰 What is the currency of Pakistan?", "options": ["Rupee", "Dollar", "Taka", "Riyal"], "answer": "Rupee"},
    {"question": "🌆 Which city is known as the 'City of Lights' in Pakistan?", "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"], "answer": "Karachi"},
    {"question": "🌍 Which country shares the longest border with Pakistan?", "options": ["India", "China", "Afghanistan", "Iran"], "answer": "India"},
    {"question": "🗺️ Which is the largest province of Pakistan by area?", "options": ["Punjab", "Sindh", "Balochistan", "KPK"], "answer": "Balochistan"},
    {"question": "🎼 Who wrote the national anthem of Pakistan?", "options": ["Hafeez Jalandhari", "Allama Iqbal", "Faiz Ahmed Faiz", "Ahmad Faraz"], "answer": "Hafeez Jalandhari"},
    {"question": "🏔️ Which is the highest mountain in Pakistan?", "options": ["K2", "Nanga Parbat", "Rakaposhi", "Gasherbrum"], "answer": "K2"},
    {"question": "🐦 Which is the national bird of Pakistan?", "options": ["Eagle", "Sparrow", "Chukar", "Peacock"], "answer": "Chukar"},
    {"question": "⚛️ In which year did Pakistan conduct nuclear tests?", "options": ["1998", "1999", "2000", "2001"], "answer": "1998"},
    {"question": "🌊 Which sea is located south of Pakistan?", "options": ["Arabian Sea", "Caspian Sea", "Red Sea", "Mediterranean Sea"], "answer": "Arabian Sea"},
    {"question": "🍽️ Which Pakistani city is famous for its 'Food Street'?", "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], "answer": "Lahore"},
    {"question": "🏞️ Which river is the longest in Pakistan?", "options": ["Jhelum", "Chenab", "Indus", "Ravi"], "answer": "Indus"},
    {"question": "🏑 What is the national sport of Pakistan?", "options": ["Hockey", "Cricket", "Football", "Kabaddi"], "answer": "Hockey"},
    {"question": "🏜️ Which desert is located in Pakistan?", "options": ["Thar", "Sahara", "Gobi", "Atacama"], "answer": "Thar"},
    {"question": "🕌 Which festival marks the end of Ramadan?", "options": ["Eid-ul-Fitr", "Eid-ul-Adha", "Ashura", "Shab-e-Miraj"], "answer": "Eid-ul-Fitr"},
    {"question": "🏆 Which Pakistani scientist won the Nobel Prize in Physics?", "options": ["Dr. Abdul Qadeer Khan", "Dr. Atta-ur-Rahman", "Dr. Abdus Salam", "Dr. Samar Mubarakmand"], "answer": "Dr. Abdus Salam"},
    {"question": "🏞️ Which lake is the largest in Pakistan?", "options": ["Saif-ul-Malook", "Manchar Lake", "Attabad Lake", "Rawal Lake"], "answer": "Manchar Lake"},
]

# 🔄 Session State Initialization
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# 📌 Get Current Question
question = st.session_state.current_question
st.subheader(f"❓ {question['question']}")

# 📌 Answer Selection
selected_option = st.radio("📌 Choose your answer:", question["options"], key="answer")

# 🎯 Submit Button
if st.button("🚀 Submit Answer"):
    st.session_state.attempts += 1
    
    if selected_option == question["answer"]:
        st.session_state.score += 1
        st.success("✅ Correct! 🎉")
    else:
        st.error(f"❌ Incorrect! The correct answer is **{question['answer']}**")
    
    # ⏳ Add Delay before next question
    time.sleep(2)
    st.session_state.current_question = random.choice(questions)
    st.rerun()

# 🎯 Score Display
st.sidebar.title("📊 Quiz Stats")
st.sidebar.write(f"🟢 Score: {st.session_state.score}")
st.sidebar.write(f"🔄 Attempts: {st.session_state.attempts}")
st.sidebar.write("💡 Keep Going! ✨")
