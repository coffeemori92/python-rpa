from imap_tools import MailBox
from account import *

applicant_list = []

with MailBox('imap.gmail.com', 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
    index = 1 # 순번
    for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)'):
        if 'hi' in msg.subject:
            nickname, phone = msg.text.strip().split('/')
            print(f'순번 : {index}, 닉네인 : {nickname}, 전화번호 : {phone}')
            applicant_list.append((msg, index, nickname, phone))
            index += 1

for applicant in applicant_list:
    print(applicant)
