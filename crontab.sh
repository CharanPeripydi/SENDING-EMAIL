crontab -e

# Send email at 9 AM Monday to Friday
0 9 * * 1-5 /usr/bin/python3 /home/ubuntu/send_email.py

# Send email at 5 PM Monday to Friday
0 17 * * 1-5  /usr/bin/python3 /home/ubuntu/send_email.py

