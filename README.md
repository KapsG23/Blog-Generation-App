# Blog Generation App 📝✨

> Turn a small idea into a full-length blog post — using a simple, friendly web app powered by AI.  
> Designed so clearly that even a 5th grader could rebuild it from scratch.

---

## 🚀 One-line Pitch

**Type a topic → Click Generate → Get a polished blog instantly.**

Fast. Fun. Beginner-friendly. Perfect for students, creators, and devs experimenting with LLMs.

---

## 📸 Demo (Optional)

_Add a GIF or screenshot of the app here._

---

## 🔖 What’s Inside This Repository?

This project is made of a few important pieces:

- **`app.py`** → The main web interface (UI) of the app.  
- **`main.py`** → The backend logic: sends your topic to the AI model and returns a blog.  
- **`src/` folder** → Helpful utilities, prompt templates, custom functions, etc.  
- **`langgraph.json`** → (If used) Defines a workflow or chain for the model.  
- **`requirements.txt` / `pyproject.toml`** → Lists all Python packages your app needs.

Everything is organized to be easy to read, modify, and extend.

---

## ✅ Quick Start Guide

> Make sure you have **Python 3.10+** installed.

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/KapsG23/Blog-Generation-App.git
```

### **2️⃣ Install, Create and Activate the UV package**

```bash
pip install uv
```

### **Create a virtual environment**

```bash
uv venv
```

### **Activate it**

```bash
.venv\Scripts\activate
```

### **Initialize the UV environment**

```bash
uv init
```

### **3️⃣ Install all dependencies**

```bash
uv add -r requirements.txt
```

### **4️⃣ Run the App**

```bash
python app.py
```

** Open the PostMan App **

** In new CLI **
```bash
langgraph dev
```

🎉 The app should now open automatically at:
- `http://127.0.0.1:8000` (FastAPI)

## 📂 File Map (Plain English)

| File / Folder      | What It Does                                             |
| ------------------ | -------------------------------------------------------- |
| `app.py`           | Builds the UI and takes your input.                      |
| `main.py`          | Talks to the AI, processes the blog, outputs text.       |
| `src/`             | Helper functions, templates, utilities.                  |
| `langgraph.json`   | Optional workflow configuration.                         |
| `requirements.txt` | Project dependencies.                                    |

## 🧠 How the Logic Works

Behind the scenes:

- A **structured prompt** is created
- The AI fills each section (intro, headings, body, conclusion)
- The response is **cleaned and formatted**
- Output is shown in the UI

This modular design makes your app easy to extend.

---

## 🖋️ Try These Sample Topics

- “How students can stay focused while studying”
- “Why sleep is important for health”
- “The future of electric vehicles”
- “How AI will change education”

## ⚠️ Common Issues & Fixes

| Issue            | Fix                                                                        |
| ---------------- | -------------------------------------------------------------------------- |
| Import errors    | Run: `uv add -r requirements.txt` again                               |
| Model not found  | Check model path or API key                                                |
| Slow output      | Reduce tokens or choose a smaller model                                    |

## ❤️ Credits

Made with love for creators, developers, and learners exploring LLMs.  
Feel free to improve, remix, and build on top of this project.

**Happy building! 🚀✨**
