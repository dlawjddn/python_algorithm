"""
문제: 땅따먹기
"""
def solution(land):
    answer = 0
    dp = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    for y in range(len(dp)):
        for x in range(len(dp[0])):
            if y == 0:
                dp[y][x] = land[y][x]
            else:
                max_value = 0
                for i in range(0, 4):
                    if i == x:
                        continue
                    else:
                        max_value = max(max_value, dp[y-1][i])
                dp[y][x] = land[y][x] + max_value
    for i in range(0, 4):
        answer = max(dp[len(dp)-1][i], answer)
    return answer