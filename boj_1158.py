from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
ans = list()
while q:
    q.rotate(-1 * (k-1))
    ans.append(q.popleft())
print(f"<{', '.join(map(str, ans))}>")

