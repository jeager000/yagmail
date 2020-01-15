import yagmail

x=yagmail.SMTP('email_sender@gmail.com','password')
subject='example'
body=str(input('Your message: '))
x.send('email_receiver@gmail.com',subject,body)
print('Success')
