import smtplib, ssl
import getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "pythontest1808"
receiver_email = "evillamorm@gmail.com"
password = getpass.getpass("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""


# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login("pythontest1808", password)
    server.sendmail(sender_email, receiver_email, message)