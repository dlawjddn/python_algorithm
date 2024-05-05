"""
문제: 피로도
"""
"""
answer = 0
def dfs(k, nums, dungeons, visited):
    if len(nums) == len(dungeons):
        temp_answer = 0
        for i in nums:
            need = dungeons[i][0]
            cost = dungeons[i][1]
            if need <= k:
                temp_answer += 1
                k -= cost
            else:
                return
        global answer
        answer = max(answer, temp_answer)
    
    for i in range(0, len(dungeons)):
        if visited[i] == 0:
            visited[i] = len(nums) + 1
            nums.append(i)
            dfs(k, nums, dungeons, visited)
            visited[i] = 0
            nums.pop()
            
            
    
def solution(k, dungeons):
    global answer
    visited = [0] * len(dungeons)
    dfs(k, [], dungeons, visited)
    return answer
"""
# 정답 1 -> 재귀를 이용한 방법
answer = 0


def dfs(k, cnt, dungeons, visited):
    global answer
    answer = max(answer, cnt)

    for i in range(len(dungeons)):
        if visited[i] == 0 and k >= dungeons[i][0]:
            visited[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = 0


def solution(k, dungeons):
    visited = [0] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer


# 정답 2 permutation을 이용한 방법
from itertools import permutations


def solution(k, dungeons):
    answer = -1
    for p in permutations(dungeons, len(dungeons)):
        temp_answer = 0
        hp = k
        for need, cost in p:
            if need <= hp:
                hp -= cost
                temp_answer += 1
            else:
                break
        answer = max(answer, temp_answer)

    return answer