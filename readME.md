# 🧠 Mindlog

**Mindlog** is a simple terminal-based journaling app for logging your thoughts and tracking your mood (from 1 to 10). It's designed to be fast, minimal, and privacy-friendly.

---

## 🚀 Features

- Log thoughts with mood level (1–10)
- Input validation and feedback
- Saves entries to a local `.json` file
- Displays the 10 most recent entries
- Built with [`Textual`](https://github.com/Textualize/textual) TUI framework

---

## 🛠 Installation

Make sure you have **Python 3.10+** (Python 3.11+ recommended).

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mindlog.git
cd mindlog
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python tui.py
```

---

## 📁 Project Structure

```
mindlog/
├── mindlog.py       # Logic for storing and loading entries
├── tui.py           # TUI interface
├── entries.json     # Entry storage (auto-created)
├── README.md
└── requirements.txt
```

---

## 🧠 Storage Format

Entries are saved in a file called `entries.json` like this:

```json
[
  {
    "timestamp": "2025-07-26 03:14",
    "thought": "Feeling productive today!",
    "mood": 8
  }
]
```

---

## 📦 TODO

- [ ] Search by keywords
- [ ] Export to Markdown or CSV
- [ ] Mood trends and graph visualization

---

## 💡 License

MIT License — free to use, modify, and share.