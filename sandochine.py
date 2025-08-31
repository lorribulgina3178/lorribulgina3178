#!/usr/bin/env python3
"""
Send one HTML e-mail via localhost:25 (Postfix, no auth).
Environment:
  MAIL_TO  – single recipient
  SUBJECT  – subject line
  HTML_PATH – HTML file to send
"""
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

TO        = os.environ["MAIL_TO"]
SUBJECT   = os.getenv("SUBJECT", "Newsletter")
HTML_PATH = Path(os.getenv("HTML_PATH", "html/newsletter.html"))
FROM_ADDR = os.getenv("FROM_ADDR", "noreply@example.com")

msg = EmailMessage()
msg["From"]    = FROM_ADDR
msg["To"]      = TO
msg["Subject"] = SUBJECT
msg.set_content("Your e-mail client does not support HTML.")
msg.add_alternative(HTML_PATH.read_text(), subtype="html")

try:
    with smtplib.SMTP("localhost", 25) as smtp:
        smtp.send_message(msg)
    print(f"✅ SENT    {TO}")
except Exception as e:
    print(f"❌ FAILED  {TO}  ({e})")
