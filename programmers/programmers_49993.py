"""
문제: 스킬트리

문자열에 속했는지 판단은 in
"""


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        temp_skill = ""
        for c in skill_tree:
            if c in skill:
                temp_skill += c
        if temp_skill == skill[:len(temp_skill)]:
            # print(temp_skill)
            answer += 1

    return answer