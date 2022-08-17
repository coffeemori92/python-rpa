import mailbox
from imap_tools import MailBox
from account import *

# mailbox = MailBox('imap.gmail.com', 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX')

# mailbox.logout()

with MailBox('imap.gmail.com', 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
    
    # for msg in mailbox.fetch(): # 전체 메일 다 가져오기
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # for msg in mailbox.fetch('(UNSEEN)'): # 읽지 않은 메일 다 가져오기
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # for msg in mailbox.fetch('(FROM aaa@gmail.com)', limit=3, reverse=True): # 특정인이 보낸 메일 가져오기
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # 띄어쓰기로 구분하여 "test", "mail"이라는 
    # 각각의 단어를 포함하는 메일을 찾음
    # for msg in mailbox.fetch('(TEXT "test mail")'): # 어떤 글자를 포함하는 메일 (제목, 본문)
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # for msg in mailbox.fetch('(SUBJECT "test mail")'): # 어떤 글자를 포함하는 메일 (제목만)
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # 영어가 아니면 필터링 해야함
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if '테스트' in msg.subject:
    #         print(f'[{msg.from_}] {msg.subject}')
            
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)'): # 특정 날짜 이후의 메일
    #     print(f'[{msg.from_}] {msg.subject}')
        
    # for msg in mailbox.fetch('(ON 07-Nov-2020)'): # 특정 날짜에 온 메일
    #     print(f'[{msg.from_}] {msg.subject}')
        
    # for msg in mailbox.fetch('(ON 07-Nov-2020)'): # 특정 날짜에 온 메일
    #     print(f'[{msg.from_}] {msg.subject}')
        
    # 2가지 이상의 조건을 모두 만족하는 메일
    # for msg in mailbox.fetch('(ON 07-Nov-2020 SUBJECT "test mail")'): # 특정 날짜에 온 메일
    #     print(f'[{msg.from_}] {msg.subject}')
        
    # 2가지 이상의 조건중 하나라도 만족하는 메일
    for msg in mailbox.fetch('(OR ON 07-Nov-2020 SUBJECT "test mail")'): # 특정 날짜에 온 메일
        print(f'[{msg.from_}] {msg.subject}')
