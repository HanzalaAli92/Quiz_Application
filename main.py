import streamlit as st
import random
import time

# Title of the Application
st.title("📝 Quiz Application")

# Define quiz questions, options, and answer in the form of a list of dictionaries
questions = [
    {
        "question": "What is the capital of Pakistan?", 
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], 
        "answer": "Islamabad",
    },
    {   
        "question": "Who is the founder of Pakistan?", 
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"],
        "answer": "Muhammad Ali Jinnah",
    },
    {   
        "question": "Which is the national language of Pakistan?", 
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"], 
        "answer": "Urdu",
    },
    {   
        "question": "What is the currency of Pakistan?", 
        "options": ["Rupee", "Dollar", "Taka", "Riyal"], 
        "answer": "Rupee",
    },
    {   
        "question": "Which city is known as the City of Lights in Pakistan?", "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"], 
        "answer": "Karachi",
    },
    {   
        "question": "Which country shares the longest border with Pakistan?", "options": ["India", "China", "Afghanistan", "Iran"], 
        "answer": "India",
    },
    {   
        "question": "Which is the largest province of Pakistan by area?", 
        "options": ["Punjab", "Sindh", "Balochistan", "KPK"], 
        "answer": "Balochistan",
    },
    {   
        "question": "Who wrote the national anthem of Pakistan?", 
        "options": ["Hafeez Jalandhari", "Allama Iqbal", "Faiz Ahmed Faiz", "Ahmad Faraz"], 
        "answer": "Hafeez Jalandhari",
    },
    {   
        "question": "Which is the highest mountain in Pakistan?", 
        "options": ["K2", "Nanga Parbat", "Rakaposhi", "Gasherbrum"], 
        "answer": "K2",
    },
    {
        "question": "Which is the national bird of Pakistan?", 
        "options": ["Eagle", "Sparrow", "Chukar", "Peacock"], 
        "answer": "Chukar",
    },
    {   
        "question": "In which year did Pakistan conduct nuclear tests?", 
        "options": ["1998", "1999", "2000", "2001"], 
        "answer": "1998",
    },
    {   
        "question": "Which sea is located south of Pakistan?", 
        "options": ["Arabian Sea", "Caspian Sea", "Red Sea", "Mediterranean Sea"], "answer": "Arabian Sea",
    },
    {   
        "question": "Which Pakistani city is famous for its 'Food Street'?", 
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], 
        "answer": "Lahore",
    },
    {   
        "question": "Which river is the longest in Pakistan?", 
        "options": ["Jhelum", "Chenab", "Indus", "Ravi"], 
        "answer": "Indus",
    },
    {   
        "question": "What is the national sport of Pakistan?", 
        "options": ["Hockey", "Cricket", "Football", "Kabaddi"], 
        "answer": "Hockey",
    },
    {   
        "question": "Which desert is located in Pakistan?", 
        "options": ["Thar", "Sahara", "Gobi", "Atacama"], 
        "answer": "Thar",
    },
    {   
        "question": "Which festival marks the end of Ramadan?", 
        "options": ["Eid-ul-Fitr", "Eid-ul-Adha", "Ashura", "Shab-e-Miraj"], 
        "answer": "Eid-ul-Fitr",
    },
    {   
        "question": "Which Pakistani scientist won the Nobel Prize in Physics?", "options": ["Dr. Abdul Qadeer Khan", "Dr. Atta-ur-Rahman", "Dr. Abdus Salam", "Dr. Samar Mubarakmand"], 
        "answer": "Dr. Abdus Salam",
    },
    {   "question": "Which lake is the largest in Pakistan?", 
        "options": ["Saif-ul-Malook", "Manchar Lake", "Attabad Lake", "Rawal Lake"], "answer": "Manchar Lake",
    },
]

# Initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio buttons for the options
selected_option = st.radio("Choose your answer", question["options"], key="answer")

# Submit button the check the answer
if st.button("Submit Answer"):
    # check if the answer is correct
    if selected_option == question["answer"]:
        st.success("✅Correct!")
    else:
        st.error("❌ Incorrect the correct answer is" +" "+ question["answer"])
    
    # Wait for 3 seconds before showing the next question
    time.sleep(3)
    
    # Select a new random question
    st.session_state.current_question = random.choice(questions)
    
    # Rerun the app to display the next question
    st.rerun()
    
