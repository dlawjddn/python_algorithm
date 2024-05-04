"""
문제: 점프와 순간 이동

1. 2의 배수인 경우 순간이동을 한 것 최소인 경우
2. 2의 배수가 아닌 경우 배터리 1을 사용해서 이동한 것이 최소인 경우

결론: 좀 더 생각하자..
"""


def solution(n):
    answer = 0
    while n > 0:
        answer += n % 2
        n //= 2
    return answer

