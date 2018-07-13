import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):
	
	def process_message(self, peer, mailfrom, rcpttos, data):
		print 'Receiving message from:', peer
		print 'Message address from:  ', mailfrom
		print 'Message address to:    ', rcpttos
		print 'Message length:        ', len(data)
		return

server = CustomSMTPServer(('10.0.0.83', 25), None)

asyncore.loop()
