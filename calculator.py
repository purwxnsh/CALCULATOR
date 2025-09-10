import streamlit as st
import math

st.set_page_config(page_title="Professional Calculator", layout="centered")

# ----------------- Custom CSS -----------------
st.markdown("""
<style>
body {
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: black;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.stButton>button {
    border-radius: 25px;
    padding: 20px;
    font-size: 22px;
    font-weight: bold;
    margin: 5px;
    transition: 0.3s;
    position: relative;
    overflow: hidden;
}
.stButton>button::after {
    content: "";
    position: absolute;
    background: rgba(255,255,255,0.3);
    border-radius: 50%;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    transform: scale(0);
    transition: transform 0.5s;
}
.stButton>button:active::after {
    transform: scale(1);
    transition: 0s;
}
.display-box {
    background-color: rgba(255,255,255,0.7);
    border-radius: 20px;
    padding: 15px;
    font-size: 28px;
    text-align: right;
    margin-bottom: 20px;
    color: black;
    min-height: 50px;
}
.footer {
    text-align: center;
    font-size: 12px;
    color: white;
    margin-top: 50px;
    opacity: 0.8;
}
.glow-red {
    color: red;
    font-weight: bold;
    animation: glow 2s ease-in-out infinite alternate;
}
@keyframes glow {
    from { text-shadow: 0 0 5px red; }
    to { text-shadow: 0 0 20px red, 0 0 30px crimson; }
}
</style>
""", unsafe_allow_html=True)

# ----------------- Header -----------------
st.markdown("<h1 style='color: #FFAE2B; text-align: center;'>🧮 Professional Calculator 🧮</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; color: white;'>Fast, colorful, fun, and feature-rich!</p>", unsafe_allow_html=True)

# ----------------- Calculator Logic -----------------
if 'calc_input' not in st.session_state:
    st.session_state.calc_input = ''
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_input(symbol):
    st.session_state.calc_input += str(symbol)

def clear_input():
    st.session_state.calc_input = ''

def calculate():
    try:
        expr = st.session_state.calc_input.replace("√","math.sqrt").replace("^","**").replace("%","/100")
        result = str(eval(expr))
        st.session_state.history.append(f"{st.session_state.calc_input} = {result}")
        st.session_state.calc_input = result
    except:
        st.session_state.calc_input = "Error"

# ----------------- Display -----------------
st.markdown(f"<div class='display-box'>{st.session_state.calc_input}</div>", unsafe_allow_html=True)

# ----------------- Buttons -----------------
buttons = [
    ["7️⃣","8️⃣","9️⃣","➗","%"],
    ["4️⃣","5️⃣","6️⃣","✖️","√"],
    ["1️⃣","2️⃣","3️⃣","➖","^"],
    ["0️⃣",".","C","=","➕"]
]

for row in buttons:
    cols = st.columns(len(row))
    for i, button in enumerate(row):
        with cols[i]:
            if st.button(button):
                if button == "C":
                    clear_input()
                elif button == "=":
                    calculate()
                else:
                    add_to_input(button.replace("➗","/").replace("✖️","*").replace("➖","-").replace("➕","+").replace("√","√").replace("^","^").replace("%","%").replace("️⃣",""))

# ----------------- History -----------------
if st.session_state.history:
    st.markdown("<h4 style='text-align:center; margin-top:20px;'>📜 Calculation History</h4>", unsafe_allow_html=True)
    for item in reversed(st.session_state.history[-10:]):
        st.markdown(f"<p style='text-align:right; margin:0px;'>{item}</p>", unsafe_allow_html=True)

# ----------------- Footer -----------------
st.markdown("""
<div class="footer">
    © 2025 Calculator Project | Design by 
    <span class="glow-red">PURWANSH CHAUDHARY</span> | Made with ❤️ in Python & Streamlit
</div>
""", unsafe_allow_html=True)
