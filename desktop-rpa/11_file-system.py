import os
import time
import datetime
import fnmatch
import shutil

# print(os.getcwd()) # current working directory 현재 작업공간

# os.chdir('../') # 부모 폴더로 이동
# print(os.getcwd())

# os.chdir('C:/') # 주어진 절대 경로로 이동
# print(os.getcwd())

# 파일 경로
# file_path = os.path.join(os.getcwd(), 'out') # 절대 경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r'C:\test\test.text'))

# 파일의 생성 날짜
# os.chdir('out')
# print(os.getcwd())
# ctime = os.path.getctime('run.png')
# print(ctime)
# # 날짜 정보를 strftime을 통해서 연월일 시분초로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime('%Y%m%d %H:%M:%S'))

# # 파일의 수정 날짜
# mtime = os.path.getmtime('run.png')
# print(datetime.datetime.fromtimestamp(mtime).strftime('%Y%m%d %H:%M:%S'))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime('run.png')
# print(datetime.datetime.fromtimestamp(atime).strftime('%Y%m%d %H:%M:%S'))

# # 파일 크기
# size = os.path.getsize('run.png')
# print(size)

# 파일 목록 가져오기
# print(os.listdir())
# print(os.listdir('out'))

# result = os.walk('.')
# print(result)

# for root, dirs, files in result:
#     print('root', root)
#     print('dirs', dirs)
#     print('files', files)
    
# 특정 폴더 내에서 특정 파일들을 찾으려면
# name = '11_file-system.py'
# result = []
# for root, dirs, files in os.walk('.'):
#     if name in files: 
#         result.append(os.path.join(root, name))
        
# print(result)

# 특정패턴 찾기
# *.xlsx, *.txt, 자동화*.png
# pattern = '*.py' # .py로 끝나는 모든 파일
# result = []

# for root, dirs, files in os.walk(os.getcwd()):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): 
#             result.append(os.path.join(root, name))
            
# for file in result:
#     print(file)

# 주어진 경로가 파일인지 폴더인지    
# print(os.path.isdir('11_file-system.py'))
# print(os.path.isfile('11_file-system.py'))

# 주어진 경로가 존재하는지
# if os.path.exists('11_file-system.py'):
#     print('파일 또는 폴더가 존재합니다.')
# else:
#     print('존재하지 않습니다.')

# 파일 만들기
# open('./out/new_file.txt', 'a').close() # 빈 파일 생성

# # 파일명 변경하기
# os.rename('./out/new_file.txt', './out/new_file_rename.txt')

# 파일 삭제하기
# os.remove('./out/new_file_rename.txt')

# 폴더 만들기
# os.mkdir('new_folder')

# 하위 폴더를 가지는 폴더 생성
# os.makedirs('new_folders/a/b/c')

# 폴더명 변경하기
# os.rename('new_folder', 'new_folder_rename')

# 폴더 지우기
# os.rmdir('new_folder_rename') # 폴더 안이 비었을 때만 삭제 가능

# 폴더 안이 비어 있지 않아도 완전 삭제 가능 
# shutil.rmtree('new_folders')

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy('./out/run.png', './test_folder')
# 새로운 파일 이름으로 복사하기
# shutil.copy('./out/run.png', './test_folder/copied_run.png')

# shutil.copyfile('./out/run.png', './test_folder/copied_run_2.png')

# copy, copyfile : 메타정보 복사x
# copy2 : 메타정보 복사O
# shutil.copy2('./out/run.png', './test_folder/copy2.png')

# 폴더 복사
# shutil.copytree('test_folder', 'test_folder2')
# shutil.copytree('test_folder', 'test_folder3')

# 폴더 이동
# shutil.move('test_folder', 'test_folder3')
# shutil.move('test_folder2', 'test_folder3')
shutil.move('test_folder3', 'test_folder') # 폴더명이 변경되는 효과
