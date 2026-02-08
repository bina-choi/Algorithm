import sys
input = sys.stdin.readline

#입력값
r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

#방향 이동키
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#방문 알파벳(현재 DFS 경로에서만 사용 중인 알파벳 집합)
visited = set()

#dfs 로직
def dfs(x, y):
    #방문 처리
    visited.add(board[x][y])
    #현재 위치에서의 최대 이동 길이 (자기 자신 포함)
    max_length = 1 

    #4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #nx, ny가 범위 안에 있고 방문 전이라면:
        if 0<=nx<r and 0<=ny<c and board[nx][ny] not in visited:
            length = 1 + dfs(nx, ny)
            max_length = max(length, max_length)
    
    #백트래킹
    visited.remove(board[x][y])

    return max_length

answer = dfs(0,0)
print(answer)
