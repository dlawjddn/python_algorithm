card = int(input())
price = list(map(int, input().split()))
dp = [0] * (card + 1)
price.insert(0, 0)


def find_max(limit):
    for i in range(1, limit + 1):
        temp_max = 0
        for j in range(1, i + 1):
            if j == 1:
                temp_max = i * price[j]
            elif j == i:
                if temp_max < price[j]:
                    temp_max = price[j]
            else:
                if temp_max < price[j] + dp[i - j]:
                    temp_max = price[j] + dp[i - j]
        dp[i] = temp_max


find_max(card)
print(dp[card])