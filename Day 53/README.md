# Day 53: Email automation concepts

Learned how Python's `smtplib` can send emails programmatically
(using an app password, not your real password, for security).
Wrote out the structure without hardcoding real credentials:

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello from Python!")
msg["Subject"] = "Test"
msg["From"] = "krishna.saini2023@sait.ac.in"
msg["To"] = "jatin.panchal2023@sait.ac.in"

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# server.login("krishna.saini2023@sait.ac.in", "app_password")
# server.send_message(msg)
# server.quit()