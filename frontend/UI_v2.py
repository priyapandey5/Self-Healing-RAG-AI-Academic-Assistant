import streamlit as st
import requests

# ----------------------------------
# Backend URL
# ----------------------------------

try:
    BACKEND_URL = st.secrets["BACKEND_URL"]
except:
    BACKEND_URL = "http://127.0.0.1:8000"

# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title="AI Academic Assistant",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------------
# Session State
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    st.title("🎓 AI Academic Assistant")

    st.markdown("---")

    st.subheader("Ask About")

    st.markdown("""
- Admissions
- Fee Structure
- Faculty Information
- Academic Calendar
- Student Policies
- Scholarships
- NEET Preparation
- JEE Preparation
- Study Materials
""")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# ----------------------------------
# Main Header
# ----------------------------------

st.title("🎓 AI Academic Assistant")

st.markdown(
    """
Welcome to the Academic Support Assistant.

Ask questions related to:

✅ Admissions

✅ Fees & Scholarships

✅ Faculty Information

✅ Academic Calendar

✅ Student Policies

✅ NEET Preparation

✅ JEE Preparation

✅ Study Resources
"""
)

# ----------------------------------
# Display Messages
# ----------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.write(
            message["content"]
        )

# ----------------------------------
# User Input
# ----------------------------------

user_message = st.chat_input(
    "Ask your question..."
)

# ----------------------------------
# Send Message
# ----------------------------------

if user_message:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message("user"):
        st.write(user_message)

    payload = {
        "user_id": "student",
        "session_id": "academic_session",
        "message": user_message
    }

    try:

        response = requests.post(
            f"{BACKEND_URL}/chat",
            json=payload
        )

        if response.status_code == 200:

            ai_reply = response.json()[
                "reply"
            ]

        else:

            ai_reply = (
                f"Backend Error: "
                f"{response.status_code}"
            )

    except Exception as e:

        ai_reply = str(e)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    with st.chat_message(
        "assistant"
    ):
        st.write(ai_reply)