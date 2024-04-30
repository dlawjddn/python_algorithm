"""
문제: 1,2,3 더하기 5
1. dp를 더 연구해보자..
2. 조금 더 세분화해서 생각할 수 있는 계기가 되길..
"""
dp = [[0 for i in range(0, 3)] for j in range(0, 100001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]


def find_ways():
    for i in range(4, 100001):
        # 1 작은 수가 2와 3으로 끝나는 경우 뒤에 1을 더하기
        dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
        # 2 작은 수가 1와 3으로 끝나는 경우 뒤에 2를 더하기
        dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
        # 3 작은 수가 1와 2로 끝나는 경우 뒤에 3을 더하기
        dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009


find_ways()
test_case = int(input())
for i in range(0, test_case):
    goal = int(input())
    print((dp[goal][0] + dp[goal][1] + dp[goal][2]) % 1000000009)
