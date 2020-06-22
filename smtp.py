import smtplib
import datetime

gmail_user = 'elsa.florea11@gmail.com'
gmail_password = 'zcrvpwhmuwmjhicq'

sent_from = gmail_user
to = ['elsa.florea11@gmail.com']
subject = 'Miscare neautorizata detectata'
body = 'Miscare neautorizata la '

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

log_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:
    print ('Something went wrong...')
