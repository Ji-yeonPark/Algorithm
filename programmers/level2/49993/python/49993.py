# -*- encoding: utf8 -*-
# Solution
# 스택을 이용해서 해결
# skill tree에 스킬 index번호를  word_idx 리스트에 삽입 
# index 번호가 순서대로 입력됬을 경우 answer + 1
# -- 
# 선행 스킬 순서 skill의 길이는 2 이상 26 이하이며, 스킬은 중복해 주어지지 않기 때문에 
# skill이 포함되지 않은 경우 27로 설정

def solution(skill, skill_trees):
    answer = 0
    
    for word in skill_trees:
        word_idx = []
        for sk in skill:
            idx = word.find(sk)
            idx = 27 if idx == -1 else idx
            word_idx.append(idx)
            
        if word_idx == sorted(word_idx):
            answer += 1
    return answer

if __name__ == '__main__':

    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

    answer = solution(skill, skill_trees)
    print "answer : ", answer 
