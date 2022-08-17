import smtplib
from imap_tools import MailBox
from email.message import EmailMessage
from openpyxl import Workbook
from account import *

max_val = 3
applicant_list = []

with MailBox('imap.gmail.com', 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
    index = 1 # 순번
    for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)'):
        if 'hi' in msg.subject:
            nickname, phone = msg.text.strip().split('/')
            print(f'순번 : {index}, 닉네인 : {nickname}, 전화번호 : {phone}')
            applicant_list.append((msg, index, nickname, phone))
            index += 1

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    for applicant in applicant_list:
        to_addr = applicant[0].from_ # 수신 메일 주소
        # index = applicant[1]
        # nickname = applicant[2]
        # phone = applicant[3]
        index, nickname, phone = applicant[1:]
        
        title = None
        content = None
        
        if index <= max_val:
            title = 'ok'
            content = f'{nickname}님 ok 선정순번 {index}번'
        else:
            title = 'fail'
            content = f'{nickname}님 fail 대기순번 {index - max_val}'
        
        msg = EmailMessage()
        msg['Subject'] = title
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_addr
        msg.set_content(content)
        
        smtp.send_message(msg)
        
wb = Workbook()
ws = wb.active

ws.append(['순번', '닉네임', '전화번호'])

for applicant in applicant[:max_val]:
    ws.append(applicant[1:])
    
    
wb.save('./out/result.xlsx')
