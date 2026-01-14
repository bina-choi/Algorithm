from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    #방문 가능 map 만들기
    field = [[-1]*102 for _ in range(102)] #2배 적용
    
    #테두리는 1, 내부는 0 (그리고 2배 적용은 기본)
    for i in rectangle:
        x1, y1, x2, y2 = map(lambda x : x*2 , i)
        for j in range(x1, x2+1):
            for k in range(y1, y2+1):
                if x1 < j < x2 and y1 < k < y2:
                    field[j][k] = 0
                elif field[j][k] != 0:  #여기서 바로 else문으로 가면 사각형 내부 비워두기 처리 못함
                    field[j][k] = 1 
    
    #이동 방식 (상하좌우)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    
    #큐 생성
    queue = deque()
    queue.append([characterX *2, characterY*2])
    
    #방문 리스트
    visited = [[0]*102 for _ in range(102)]
    visited[characterX *2][characterY*2] = 1 #시작 지점은 방문 표시
    
    #bfs 알고리즘 실행
    while queue:
        x, y = queue.popleft()
        
        #지점 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #while문 빠져나오기
            if x == itemX * 2 and y == itemY * 2:
                answer = visited[x][y] //2
                break
            
            #갈 수 있는 지점이고, 아직 방문 전이라면 큐 삽입 + 방문 처리
            if field[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    
    

    
    return answer