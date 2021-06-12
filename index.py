import csv

with open('emails.csv', 'r') as file:
    emails = []
    csv_reader = csv.reader(file)
    for lines in csv_reader:
        emails.append(lines[1])
    emails.pop(0)
    print(emails)


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Create the plain-text and HTML version of your message
text = """\
ENTER email body"""


html = """\
Enter HTML of the message
"""

message = MIMEMultipart("alternative")


sender = 'ENTER EMAIL HERE'
message['From'] = sender
message['To'] = ", ".join(emails)
message['Subject'] = 'Subject'


# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(sender, 'ENTER_PASSWORD_HERE')

mailserver.sendmail(sender,emails,message.as_string())

mailserver.quit()








