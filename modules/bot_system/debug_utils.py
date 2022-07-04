# 테스트/디버그용 유틸 함수 작성
import datetime

# 현재 시간
def build_time()->str:
    today = datetime.datetime.now()
    return today.strftime('%y%m%d %H:%M:%S')
    