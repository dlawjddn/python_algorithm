"""
문제: 호텔 대실
"""

"""
1차 제출
def solution(book_time):
    answer = 0
    time = [[0 for _ in range(0, 60)] for _ in range(0, 25)]
    for start, end in book_time:
        start_hour, start_minute = map(int, (start.split(":")))
        end_hour, end_minute = map(int, (end.split(":")))
        if end_minute + 10 >= 60:
            end_minute = (end_minute + 10) % 60
            end_hour += 1
        else:
            end_minute += 10
        for h in range(start_hour, end_hour + 1):
            for m in range(0, 60):
                if h == start_hour and m < start_minute:
                    continue
                if h == end_hour and m >= end_minute:
                    continue
                time[h][m] += 1

    for h in range(0, 25):
        for m in range(0, 60):
            answer = max(answer, time[h][m])

    return answer
"""
# 2차 제출 좀 더 보기 좋게
def solution(book_time):
    answer = 0
    time = [0] * (25 * 60)  # 전체 시간대를 분 단위로 표현

    for start, end in book_time:
        start_hour, start_minute = map(int, start.split(":"))
        end_hour, end_minute = map(int, end.split(":"))

        start_index = start_hour * 60 + start_minute
        end_index = end_hour * 60 + end_minute + 10

        # 시작 시간부터 종료 시간까지 해당하는 분에 예약된 횟수 증가
        for i in range(start_index, end_index):
            time[i] += 1

    # 최대 예약 횟수 찾기
    answer = max(time)

    return answer
