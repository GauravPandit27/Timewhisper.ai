import streamlit as st
from datetime import datetime, timedelta
from constants import groq_key
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# --- PAGE CONFIG ---
st.set_page_config(page_title="TimeWhisper.ai", layout="centered")

# --- LLM SETUP ---
llm = ChatGroq(api_key=groq_key, model_name="llama3-8b-8192")

# --- CSS STYLE ---
st.markdown("""
    <style>
        html, body {
            background-color: #0f1117;
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton button {
            background-color: #6c47ff;
            color: white;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            font-weight: bold;
        }
        .box {
            background-color: #1f1f2e;
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 12px;
        }
        .small {
            font-size: 13px;
            color: #999;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("⏳ TimeWhisper.ai")
st.caption("Convert your goals into a peaceful, focused daily schedule.")
st.markdown("<div class='small'>“Discipline is choosing between what you want now and what you want most.”</div><br>", unsafe_allow_html=True)

# --- SESSION STATE ---
if "schedule_history" not in st.session_state:
    st.session_state.schedule_history = []
if "project_plans" not in st.session_state:
    st.session_state.project_plans = []

# --- PROMPT TEMPLATE ---
prompt_template = """
You are TimeWhisper, an expert productivity coach and focus mentor.

User has shared daily goals, optional recurring tasks, and natural language routines. Build a time-blocked daily schedule that balances deep work, breaks, and realism.

✅ Format:
- 7:00 AM – Morning routine
- 8:00 AM – Task 1

🎯 Rules:
- Fit work within {duration_pref} hours.
- Honor user's energy peaks: {energy}
- Follow break preference: {rest}
- Prioritize recurring tasks: {recurring_tasks}
- Convert natural language routines into structured time blocks.
- Detect and reduce low-focus tasks like gaming, doomscrolling, etc.
- Adjust flow based on selected productivity mode: {mode}

🧾 After the schedule, give:
1. Why this flow is optimal
2. Advice to improve time use
3. A Focus Score out of 10
4. Micro-coaching tips to maintain discipline

Daily Goals: {tasks}
"""

prompt = PromptTemplate(
    input_variables=["tasks", "recurring_tasks", "duration_pref", "energy", "rest", "mode"],
    template=prompt_template
)
chain = LLMChain(llm=llm, prompt=prompt)

# --- DAILY SCHEDULE FORM ---
with st.form("schedule_form"):
    st.subheader("🎯 Daily Plan")
    tasks = st.text_area("🧠 What tasks/goals do you want to complete today?", placeholder="e.g. Finish project report, gym, call with client")
    recurring_tasks = st.text_area("🔁 Recurring Daily/Weekly Tasks (Optional)", placeholder="e.g. Gym, Meditation, Family Time")
    duration_pref = st.slider("🕒 Total hours you want to work today", 2, 14, 8)
    energy = st.selectbox("⚡ When are you most productive?", ["Morning", "Afternoon", "Evening", "Night Owl"])
    mode = st.selectbox("🧠 Productivity Style", ["Balanced", "Deep Work", "Pomodoro"])
    rest = st.radio("🌿 How often do you want breaks?", ["Every 2 hours", "After each task", "Only lunch break"])
    submit = st.form_submit_button("🧘 Generate My Schedule")

if submit:
    if not tasks.strip():
        st.warning("Please enter your goals/tasks to create a schedule.")
    else:
        with st.spinner("⏳ Whispering with time..."):
            response = chain.run({
                "tasks": tasks,
                "recurring_tasks": recurring_tasks or "None",
                "duration_pref": duration_pref,
                "energy": energy,
                "rest": rest,
                "mode": mode
            })
            st.session_state.schedule_history.append(response)

if st.session_state.schedule_history:
    st.subheader("📅 Your Optimized Daily Schedule")
    latest_schedule = st.session_state.schedule_history[-1].replace("\n", "<br>")
    st.markdown(f"<div class='box'>{latest_schedule}</div>", unsafe_allow_html=True)

# --- PROJECT TIME PLANNER ---
with st.form("project_planner"):
    st.subheader("🛠️ Project Time Allocator")
    project_name = st.text_input("📌 Project Name")
    total_hours = st.slider("⏱️ Total Work Required (in hours)", 1, 40, 7)
    deadline = st.date_input("📅 Deadline")
    project_submit = st.form_submit_button("📆 Allocate Project Time")

if project_submit and project_name:
    days_remaining = (deadline - datetime.today().date()).days + 1
    hours_per_day = round(total_hours / days_remaining, 2) if days_remaining > 0 else total_hours
    project_plan = f"Project: {project_name}<br>Deadline: {deadline}<br>Distribute ~{hours_per_day} hrs/day over {days_remaining} days."
    st.session_state.project_plans.append(project_plan)

if st.session_state.project_plans:
    st.subheader("📊 Project Breakdown")
    for plan in st.session_state.project_plans:
        st.markdown(f"<div class='box'>{plan}</div>", unsafe_allow_html=True)

# --- CLEAR BUTTON ---
if st.button("🧹 Start Fresh"):
    st.session_state.schedule_history = []
    st.session_state.project_plans = []
