import getpass
def send_email():
	# smtplib module send mail
    import smtplib
    print("To whom you want this email: \n")
    TO = input("")
    SUBJECT = 'TEST MAIL'
    TEXT = 'Here is a message from python.'

	# Gmail Sign In
    print("Enter Your Email: \n")
    gmail_sender = input("")
    print("Password: \n")
    gmail_passwd = getpass.getpass('')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
    BODY = '\r\n'.join(['To: %s' % TO,
                    	'From: %s' % gmail_sender,
                    	'Subject: %s' % SUBJECT,
                    	'', TEXT])
    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')
        
    server.quit()



