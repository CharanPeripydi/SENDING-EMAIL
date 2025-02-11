import smtplib
import sys
from email.mime.text import MIMEText

EMAIL_ADDRESS = "charansrinivas862@gmail.com"
EMAIL_PASSWORD = "fiov gkbi rujl zgdk"

message_text = sys.argv[1] if len(sys.argv) > 1 else "Default Message"

TO_EMAIL = "reddycharan183@gmail.com"
SUBJECT = "you can login/logout"

msg = MIMEText(message_text)
msg["From"] = EMAIL_ADDRESS
msg["To"] = TO_EMAIL
msg["Subject"] = SUBJECT

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print("Error:", e)