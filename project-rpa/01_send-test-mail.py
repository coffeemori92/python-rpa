import smtplib
from account import *
from email.message import EmailMessage
from random import *

nicknames = ['aaa', 'bbb', 'ccc']

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    for nickname in nicknames:
        msg = EmailMessage()
        msg['Subject'] = 'hi'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        
        # content = nickname + '/' + str(randint(1000, 9999))
        content = '/'.join([nickname, str(randint(1000, 9999))])
        msg.set_content(content)
        
        smtp.send_message(msg)
        print(f'{nickname}님이 {EMAIL_ADDRESS}계정으로 메일 발송 완료')
        