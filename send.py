import yagmail

x=yagmail.SMTP('cacacrackphiss@gmail.com','jeager1999$')
subject='example'
body=str(input('Your message: '))
x.send('cacacrack000@gmail.com',subject,body)
print('Success')