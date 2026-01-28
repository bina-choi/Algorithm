def solution(tickets):
    tickets.sort(key = lambda x : (x[0], x[1]))
    n = len(tickets)
    used = [0] * n
    answer = []

    
    def dfs(curr, path):
        # 종료 조건
        if len(path) == n + 1:
            return path
        
        # for문으로 조건 탐색
        for i in range(n):
            if tickets[i][0] == curr and used[i] == 0:
                used[i] = 1  #티켓 사용 처리
                result = dfs(tickets[i][1], path + [tickets[i][1]])
                used[i] = 0
                
                if result:
                    return result
                
        return None
            
    answer = dfs("ICN", ["ICN"])    
    return answer


