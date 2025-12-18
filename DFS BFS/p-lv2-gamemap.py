from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    #방향 이동 지표
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1,  1]
    
    #거리 계산 행렬
    distance = [[0] * m for _ in range(n)]
    
    queue = deque()
    queue.append((0,0)) #[0,0] 꼴도 가능하나 튜플이 더 적합
    distance[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        #목표지점 도착 시 멈춤
        if x == n-1 and y == m-1:
            return distance[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #nx, ny가 맵 범위 안에 있는지
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #벽인 경우도 pass
            if maps[nx][ny] == 0:
                continue
            #방문 여부도 체크
            if distance[nx][ny] != 0:
                continue
            
            #정상적인 nx, ny만 큐에 삽입 
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))
            
    return -1
            
            
        