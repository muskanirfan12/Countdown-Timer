import time
import streamlit as st

# Initialize session state
if "running" not in st.session_state:
    st.session_state.running = False
if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 10  # Default time

def countdown_timer():
    st.session_state.running = True  # Set running flag to True
    placeholder = st.empty()
    
    while st.session_state.remaining_time >= 0 and st.session_state.running:
        mins, secs = divmod(st.session_state.remaining_time, 60)
        placeholder.markdown(f"""
        <div style='text-align: center; font-size: 40px; font-weight: bold; color: #FF5733;'>
            ⏳ {mins:02}:{secs:02}
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1)
        st.session_state.remaining_time -= 1
    
    if st.session_state.running:
        placeholder.success("🎉 Time's Up! The countdown has finished!")
    else:
        placeholder.warning("⏹ Timer Stopped! Click 'Start' to resume.")

# Streamlit UI
st.set_page_config(page_title="Countdown Timer", page_icon="⏳", layout="centered")

st.markdown(
    "<h1 style='color: #4CAF50;'>⏳Countdown Timer⏲️</h1>", 
    unsafe_allow_html=True
)

st.markdown("<p style='font-size:18px; color:#333;'>Enter countdown time in seconds:</p>", unsafe_allow_html=True)

# Update remaining time only if the timer is not running
if not st.session_state.running:
    st.session_state.remaining_time = st.number_input(
        "", min_value=1, step=1, value=st.session_state.remaining_time, format="%d",
        key="time_input", help="Set the countdown duration in seconds."
    )

button_style = """
    <style>
        div.stButton > button {
            background-color: #008CBA;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #005f73;
        }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("Start Timer⏲️"):
        countdown_timer()

with col2:
    if st.button("Stop Timer ⏹"):
        st.session_state.running = False  # Stop the countdown

#footer
st.write("------")
st.write("Created by 💪 Muskan Irfan Ahmed 💪")        
