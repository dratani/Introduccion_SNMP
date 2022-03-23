import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
COMMASPACE = ', '
# Define param


mailsender = "dummycuenta3@gmail.com"
mailreceip = "dummycuenta3@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'Secreto123@'
subject = "Alerta SNMP-TRAP detectada"
mail_content = 'Trap detectada'

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = mailsender
msg['To'] = mailreceip
msg.attach(MIMEText(mail_content, 'plain'))
s = smtplib.SMTP(mailserver)
s.starttls()
# Login Credentials for sending the mail
s.login(mailsender, password)
s.sendmail(mailsender, mailreceip, msg.as_string())
s.quit()
print('Mail Sent')