from collections import deque

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer

def bfs(begin, target, words):
    #방문 리스트 정의
    visited = set()
    visited.add(begin) #set에는 append가 아닌 add를 사용
    
    #큐 정의
    queue = deque()
    queue.append((begin, 0))
    
    #bfs 로직
    while queue:
        curr_word, curr_idx = queue.popleft()
        
        if curr_word == target:
            return curr_idx
        
        for word in words:
            if is_one_diff(curr_word, word) and word not in visited:
                visited.add(word)
                queue.append((word, curr_idx+1))
    return 0
            

def is_one_diff(word1, word2):
    diff_cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_cnt += 1 
    if diff_cnt == 1:
        return True
    else:
        return False
        