import streamlit as st
from PIL import Image
from streamlit_chat import message  # Requires streamlit-chat module

# Page config
st.set_page_config(page_title="Xiangwen Xiong | AI Portfolio", layout="centered")

# --- Style Badges ---
st.markdown("""
<div style='text-align: center;'>
    <img src='https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white' height='30'>
    <img src='https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white' height='30'>
    <img src='https://img.shields.io/badge/Gurobi-FF0000?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgo=' height='30'>
    <img src='https://img.shields.io/badge/GPT--4-612B9B?style=for-the-badge&logo=openai&logoColor=white' height='30'>
</div>
""", unsafe_allow_html=True)

# --- Header ---
st.title("👋 Hi, I’m Xiangwen Xiong")
st.markdown("""
**Business Analyst | AI Developer | Supply Chain Optimizer**

Welcome to my portfolio! I build AI-powered decision tools that combine analytics, optimization, and machine learning to solve real-world problems.

Feel free to explore my projects below:
""")

# --- Project 1: DecisionFlow AI ---
st.header("📦 DecisionFlow: AI Assistant for Supply Chain Optimization")
st.markdown("""
A Streamlit-based chatbot that integrates GPT-4 and Gurobi to help users make cost-effective supply chain decisions without writing a single line of code.

**Key Features:**
- GPT-4 + Gurobi integration for scenario planning
- Three-layer supply chain optimization model
- Supports natural language what-if questions

🔗 [Launch App](https://decisionflow-ai-assistant.streamlit.app/)  
🔗 [GitHub Repo](https://github.com/rocker097/decisionflow-ai-assistant)
""")

# --- Project 2: FitFuel AI Coach ---
st.header("🥗 FitFuel: Personalized Nutrition & Fitness Planner")
st.markdown("""
An AI chatbot that delivers real-time meal and workout suggestions using GPT-4, nutrition APIs, and web scraping techniques. Built to scale personalized wellness planning.

**Key Features:**
- Real-time dietary recommendations
- Meal generation using Edamam and USDA APIs
- BeautifulSoup + Selenium scraping from Wikipedia

🔗 [Visit Site](https://rocker097.github.io/assingment-3-/)  
🔗 [GitHub Repo](https://github.com/rocker097/assingment-3-)
""")

# --- Chatbot Section ---
st.header("💬 Ask Me Anything")
st.markdown("""
Try asking me something about my work or skills. For example:
- What does your DecisionFlow chatbot do?
- What tools did you use for FitFuel?
""")

# Initialize chat history if not exists
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display past messages
for i, msg in enumerate(st.session_state["messages"]):
    message(msg["content"], is_user=msg["is_user"], key=str(i))

# Chat input
user_input = st.chat_input("Ask about my projects or background...")
if user_input:
    st.session_state["messages"].append({"content": user_input, "is_user": True})

    # Simple hardcoded response (replace with OpenAI if needed)
    if "decisionflow" in user_input.lower():
        bot_reply = "DecisionFlow is a chatbot that connects GPT-4 and Gurobi to solve supply chain optimization problems based on user input."
    elif "fitfuel" in user_input.lower():
        bot_reply = "FitFuel is a personal wellness planner that recommends meals and workouts using nutrition APIs and GPT-4."
    elif "tools" in user_input.lower() or "tech" in user_input.lower():
        bot_reply = "I use Python, Streamlit, GPT-4, Gurobi, and APIs like Edamam and USDA."
    else:
        bot_reply = "Thanks for your question! Feel free to ask about any of the projects."

    st.session_state["messages"].append({"content": bot_reply, "is_user": False})
    message(bot_reply, key=str(len(st.session_state["messages"])))

# --- Footer ---
st.markdown("""
---
📫 Want to get in touch? Email me at [xxion@ucdavis.edu](mailto:xxion@ucdavis.edu)
""")
