# 100 Days of Python 🐍

A daily practice log of small Python and AI/ML projects, one folder per day.
The goal: consistent, real commits — not empty ones — while building up from
core Python basics to beginner machine learning.

## 📌 How this repo works

- Each day lives in its own folder: `day-01/`, `day-02/`, etc.
- Every folder has one small, focused script (and any data files it needs).
- Progress is logged in [`PROGRESS.md`](./PROGRESS.md) — one line per day.
- Commits are made daily and pushed to `main` to keep the habit consistent.

## 🗂️ Structure

```
daily-python/
├── README.md
├── PROGRESS.md
├── day-01/
│   └── greeting.py
├── day-02/
│   └── age_check.py
├── day-03/
│   └── times_table.py
...
└── day-40/
    └── spam_classifier.py
```

## 🛠️ Setup

Some later days use external libraries. To run any script that needs them:

```bash
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Then run any day's script directly:

```bash
python day-01/greeting.py
```

## 📅 Roadmap

| Range | Focus |
|-------|-------|
| Days 1–7 | Python basics — variables, conditionals, loops, lists, functions, dicts |
| Days 8–14 | Files, error handling, strings, JSON, first mini project |
| Days 15–17 | Classes, objects, and modules |
| Days 18–20 | External libraries, APIs, and a first ML model |
| Days 21–30 | Data analysis (pandas, numpy), visualization, regression, classification |
| Days 31–37 | APIs, web scraping, testing, CLI tools, dates |
| Days 38–40 | Applied mini projects — recommender, perceptron, spam classifier |

*(Extends toward Day 100 as new topics are added.)*

## ✅ Progress

See the full day-by-day log in [`PROGRESS.md`](./PROGRESS.md).

## 🎯 Why this repo exists

To build a genuine daily coding habit — real, understandable code committed
every day — rather than empty commits just to fill a contribution graph.

## 📄 License

MIT — feel free to fork this and start your own 100 days.
