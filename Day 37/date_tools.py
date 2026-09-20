# Day 37: datetime module

from datetime import datetime, timedelta

now = datetime.now()
print(f"Today: {now.strftime('%Y-%m-%d')}")

birthday = datetime(2000, 5, 15)
days_alive = (now - birthday).days
print(f"Days since that date: {days_alive}")

next_week = now + timedelta(days=7)
print(f"One week from now: {next_week.strftime('%Y-%m-%d')}")