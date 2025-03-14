
# import streamlit as st
# import datetime
# import time

# # Title of the app
# st.title("⏰ Task Reminder App")

# # Displaying a professional image under the title
# st.image(
#     "https://img.freepik.com/premium-photo/exploding-clock-as-symbol-escaping-time-generative-ai_935190-71.jpg",
#     use_container_width=True  # Corrected parameter
# )

# # Multi-task input area
# task = st.text_input("Enter the task you want to be reminded of:")

# # Input for reminder duration (in minutes)
# reminder_duration = st.number_input("Set reminder duration (in minutes):", min_value=1, max_value=120)

# # Initialize session state for reminder
# if "reminder_time" not in st.session_state:
#     st.session_state.reminder_time = None
#     st.session_state.task = None

# # Button to set the reminder
# if st.button("Set Reminder"):
#     if task and reminder_duration:
#         # Calculate the reminder time
#         st.session_state.reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=reminder_duration)
#         st.session_state.task = task
#         st.success(f"Reminder set for '{task}' in {reminder_duration} minutes at {st.session_state.reminder_time.strftime('%I:%M %p')}!")
#     else:
#         st.warning("Please enter a task and set a reminder duration!")

# # Create a placeholder to refresh UI
# status_placeholder = st.empty()

# # Auto-refresh logic
# if st.session_state.reminder_time:
#     while True:
#         current_time = datetime.datetime.now()
#         time_remaining = (st.session_state.reminder_time - current_time).total_seconds()

#         if time_remaining <= 0:
#             # Show reminder message and balloons
#             status_placeholder.error(f"⏰ Time to: {st.session_state.task}!")
#             st.balloons()
#             # Reset reminder
#             st.session_state.reminder_time = None
#             st.session_state.task = None
#             break  # Exit loop when reminder triggers
        
#         # Show countdown timer
#         status_placeholder.info(f"⏰ Time remaining: {int(time_remaining)} seconds")
        
#         time.sleep(1)  # Sleep for 1 second before updating

# # Display the current time
# st.write("Current time:", datetime.datetime.now().strftime('%I:%M %p'))
















































import streamlit as st
import datetime
import time
import random

# Motivational messages list
motivational_messages = [
    "Mistakes are proof that you are trying! Keep going! 💪",
    "Challenges help us grow. Every step counts! 🚀",
    "Believe in your ability to improve! 🌱",
    "Hard work beats talent when talent doesn’t work hard! 🔥",
    "Every expert was once a beginner! Keep learning! 📚"
]

# Title of the app
st.title("🌟 Growth Mindset Task Reminder")

# Displaying an inspiring image
st.image(
    "https://img.freepik.com/premium-photo/exploding-clock-as-symbol-escaping-time-generative-ai_935190-71.jpg",
    use_container_width=True
)

# Multi-task input area
task = st.text_input("Enter the task you want to be reminded of:")

# Input for reminder duration (in minutes)
reminder_duration = st.number_input("Set reminder duration (in minutes):", min_value=1, max_value=120)

# Initialize session state for reminder & progress tracking
if "reminder_time" not in st.session_state:
    st.session_state.reminder_time = None
    st.session_state.task = None
    st.session_state.completed_tasks = []

# Button to set the reminder
if st.button("Set Reminder"):
    if task and reminder_duration:
        # Calculate the reminder time
        st.session_state.reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=reminder_duration)
        st.session_state.task = task
        st.success(f"Reminder set for '{task}' in {reminder_duration} minutes at {st.session_state.reminder_time.strftime('%I:%M %p')}!")
    else:
        st.warning("Please enter a task and set a reminder duration!")

# Create a placeholder to refresh UI
status_placeholder = st.empty()

# Auto-refresh logic
if st.session_state.reminder_time:
    while True:
        current_time = datetime.datetime.now()
        time_remaining = (st.session_state.reminder_time - current_time).total_seconds()

        if time_remaining <= 0:
            # Show reminder message and balloons
            status_placeholder.error(f"⏰ Time to: {st.session_state.task}!")
            st.balloons()
            st.session_state.completed_tasks.append(st.session_state.task)
            # Display a random motivational message
            st.success(random.choice(motivational_messages))
            # Reset reminder
            st.session_state.reminder_time = None
            st.session_state.task = None
            break  # Exit loop when reminder triggers
        
        # Show countdown timer
        status_placeholder.info(f"⏰ Time remaining: {int(time_remaining)} seconds")
        
        time.sleep(1)  # Sleep for 1 second before updating

# Display completed tasks & sharing option
st.subheader("✅ Completed Tasks")
if st.session_state.completed_tasks:
    for completed_task in st.session_state.completed_tasks:
        st.write(f"- {completed_task}")
    
    # Share progress on WhatsApp
    share_message = f"I just completed my task: {st.session_state.completed_tasks[-1]}! Keeping a growth mindset! 💪"
    share_url = f"https://wa.me/?text={share_message}"
    st.markdown(f"[📤 Share on WhatsApp]({share_url})", unsafe_allow_html=True)
else:
    st.write("No tasks completed yet. Keep going! 🚀")

# Display the current time
st.write("Current time:", datetime.datetime.now().strftime('%I:%M %p'))












