def solution(n, computers):
    answer = 0
    #방문 리스트
    visited = [False] * n
    
    #dfs 정의하기
    def dfs(computers, i, visited):
        visited[i] = True
        
        for k in range(len(computers[i])):
            if computers[i][k] == 1 and visited[k] != 1:
                dfs(computers, k, visited)
    
    #네트워크 개수 계산
    for i in range(n):
        if visited[i] != True:
            dfs(computers, i, visited)
            answer += 1 
            
    return answer

