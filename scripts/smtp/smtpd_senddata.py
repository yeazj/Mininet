import smtplib
import email.utils
from email.mime.text import MIMEText

msg = MIMEText('This is the body of a message')
msg['To'] = email.utils.formataddr(('Recipient', 'recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('10.0.0.83', 25)
server.set_debuglevel(True)

try:
	server.sendmail('author@example.com', ['recipient@example.com'], msg.as_string())
finally:
	server.quit()
