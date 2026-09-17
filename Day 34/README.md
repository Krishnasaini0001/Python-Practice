# Day 34: Virtual Environments

Learned how to isolate project dependencies:

python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt

This keeps each project's packages separate and makes projects reproducible for others.