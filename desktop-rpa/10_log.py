import logging
from datetime import datetime

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')

# debug < info < warning < error < critical
# logging.debug('aaaaaa')
# logging.info('자동화 수행 준비')
# logging.warning('실행상에 문제가 있을 수 있습니다.')
# logging.error('에러가 발생 하였습니다. 에러 코드는 ...')
# logging.critical('복구가 불가능한 심각한 문제가 발생했습니다.')

# 터미널과 파일에 함께 로그 남기기
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger()
# f로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

file_name = datetime.now().strftime('./out/mylogfile_%Y%m%d%H%M%S.log')
file_handler = logging.FileHandler(filename=file_name, encoding='utf-8')
logger.addHandler(file_handler)

logger.debug('로그를 남기는 테스트 진행')
