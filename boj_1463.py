from collections import deque
num = int(input())
count = [0] * (num + 1)
count[num] = 1
q = deque()
q.append(num)
while q:
    now = q.popleft()
    for i in range(1,4):
        if now <= 0:
            continue
        if  i == 1 and now % 3 == 0 and count[now // 3] == 0:
            q.append(now // 3)
            count[now // 3] = count[now] + 1
        elif i == 2 and now % 2 == 0 and count[now // 2] == 0:
            q.append(now // 2)
            count[now // 2] = count[now] + 1
        elif i == 3 and count[now - 1] == 0:
            q.append(now - 1)
            count[now - 1] = count[now] + 1
print(count[1]-1)




