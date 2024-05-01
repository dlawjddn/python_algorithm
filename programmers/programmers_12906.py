"""
문제: 같은 숫자는 싫어
"""
def solution(arr):
    ans = []
    for i in range(0, len(arr)):
        if not ans:
            ans.append(arr[i])
        else:
            if ans[-1] == arr[i]:
                continue
            else:
                ans.append(arr[i])
    return ans
