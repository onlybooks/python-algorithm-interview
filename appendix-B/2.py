def solution(dartResult: str) -> int:
    nums = [0]

    for s in dartResult:
        if s == 'S':
            nums[-1] **= 1
            nums.append(0)
        elif s == 'D':
            nums[-1] **= 2
            nums.append(0)
        elif s == 'T':
            nums[-1] **= 3
            nums.append(0)
        elif s == '*':
            # 이전 값, 그 이전 값 모두 두 배 처리
            nums[-2] *= 2
            if len(nums) > 2:
                nums[-3] *= 2
        elif s == '#':
            nums[-2] *= -1
        else:
            # 자릿수 올림
            nums[-1] = nums[-1] * 10 + int(s)

    return sum(nums)
