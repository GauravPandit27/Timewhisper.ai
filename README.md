
# ⏳ TimeWhisper.ai

**Your Intelligent Daily Planner & Focus Coach** built with **LangChain**, **Groq’s LLaMA3**, and **Streamlit**. Turn your goals into peaceful, productive schedules — without the chaos.

---

## 🚀 Features

| 🔧 Core Feature | 💡 Description |
|----------------|----------------|
| 🗓️ Natural Language Routine Parser | Converts text like “wake at 7, gym 1hr” into structured time blocks |
| ⏱️ Project-to-Time Allocation | Input: “7 hr task in 3 days” → Output: smart weekly work distribution |
| 📆 Weekly Task Planner | Add/manage recurring weekly tasks. Clean weekly breakdown |
| 🎯 Distraction Detector | Flags gaming, doomscrolling, low-focus habits — gives alternatives |
| 📈 Focus Score + Micro-Coaching | Scores each day’s schedule + provides focus tips |
| 🧘 Hustle/Peace/Monk Modes | Choose your vibe: grind, balance, or calm-reflection |

---

## 🧠 Tech Stack

- **LangChain** – Prompt templating + chaining
- **Groq + LLaMA 3-8B-8192** – Ultra-fast inference via `langchain_groq`
- **Streamlit** – Clean interactive UI
- **Python (datetime, etc.)** – For smart scheduling & time handling

---

## 📸 Screenshots

_Add a few screenshots of the app here (optional)_

---

## 🛠️ Setup & Run

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/TimeWhisper.ai.git
cd TimeWhisper.ai
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Add Your API Key

Create a file named `constants.py`:

```python
groq_key = "your-groq-api-key"
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧪 Example Input

```
Tasks: wake at 7, gym 1hr, write blog, build GenAI tool  
Recurring: meditation, reading, family dinner  
Hours: 8  
Energy: Morning  
Mode: Deep Work  
Breaks: After each task
```

---

## 🧘‍♂️ Vision

**TimeWhisper.ai** isn’t just a planner — it’s your time therapist.

Built to:

* Reduce chaos, create clarity
* Align your time with long-term goals
* Replace dopamine traps with intentional focus

---

## ✨ Credits

Created with ❤️ by **[Gaurav Pandit](https://www.linkedin.com/in/gauravpandit)**
Founder of **PAIRS (Pandit AI Research & Innovative Solutions)**

---

## 📜 License

MIT License — use it, build on it, whisper time back into your hands ✌️

```

---

Let me know if you want:
- A fancy banner image
- Notion-style documentation
- GitHub Action for auto-deployment to Streamlit Cloud

Let's make this repo founder-quality.
```
