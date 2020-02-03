### Send email with plots embedded
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import relevantstats as d
import matplotlib.pyplot as plt
import base64
from io import BytesIO

fig1 = plt.figure(d.maxplayers_by_count)
print(type(fig1))
#fig2 = d.playtime_by_count.figure()

tmpfile = BytesIO()
fig1.savefig(tmpfile, format='png')
encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "pythontest1808"
receiver_email = "evillamorm@gmail.com"
password = getpass.getpass("Type your password and press enter: ")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = ""
html = f"""\
<html>
  <body>
    <p>Hi,<br>
       These are the lastest board game graphs<br>
       <img src=\'data:image/png;base64,{fig1}\'>       
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )