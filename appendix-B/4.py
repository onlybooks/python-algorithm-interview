from typing import List


def solution(n: int, t: int, m: int, timetable: List[str]) -> str:
    # 입력값 분 단위 전처리
    timetable = [
        int(time[:2]) * 60 + int(time[3:])
        for time in timetable
    ]
    timetable.sort()

    current = 540
    for _ in range(n):
        for _ in range(m):
            # 대기가 있는 경우 1분 전 도착
            if timetable and timetable[0] <= current:
                candidate = timetable.pop(0) - 1
            else:  # 대기가 없는 경우 정시 도착
                candidate = current

        current += t
    # 시, 분으로 다시 변경
    h, m = divmod(candidate, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)
