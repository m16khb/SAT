row, col = map(int, input().split())
maze = [""] * row
for i in range(row):
    maze[i] = input() #퍼즐 저장 리스트
visited = [[0] * col for _ in range(row)] #방문 체크 리스트
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]] #상하좌우 이동범위

q = list()


def solve(i: int, j: int): #BFS 활용
    global visited
    q.append([i, j])
    visited[i][j] = 1 #방문한 곳 1
    while len(q): #큐에 값이 남아있으면 반복
        temp = q.pop(0)
        i = temp[0] #현재 퍼즐에서의 y축
        j = temp[1] #현재 퍼즐에서의 x축
        cnt = visited[i][j] #몇번 이동해서 현재위치에 도달 했는지
        if i == row - 1 and j == col - 1: #종료 조건
            print(visited[i][j])
            return
        for m in range(4): #현재 위치의 상하좌우 좌표를 대입
            dy = i + dir[m][0]
            dx = j + dir[m][1]
            if row <= dy or dy < 0 or col <= dx or dx < 0: #미로에서 벗어날 경우 거름
                continue
            if maze[dy][dx] == "1" and visited[dy][dx] == 0: #미로의 길이 연결되어 있고 방문한적이 없을 경우
                visited[dy][dx] = cnt + 1 #방문 체크 리스트에 이동한 횟수로 체크
                q.append([dy, dx]) #큐에 추가


solve(0, 0)
