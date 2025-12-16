from collections import deque

#BFS 풀이 버전
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    # 큐 정의
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0]) #인덱스를 같이 저장해두는게 편함
    
    #while queue
    while queue:
        value, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([value + numbers[idx], idx])
            queue.append([value - numbers[idx], idx])
        else:
            if value == target:
                answer += 1
    return answer


# DFS 풀이 버전
def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer
    
    
def dfs(numbers, target, depth):
    answer = 0

    #종료 조건(재귀 바닥 부분)
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0

    #핵심 재귀 로직
    else:
        # 양수라고 가정
        answer += dfs(numbers, target, depth+1)
        # 음수라고 가정
        numbers[depth] *= -1
        answer += dfs(numbers, target, depth+1)
        return answer
        
        














