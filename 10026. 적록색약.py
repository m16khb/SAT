import sys
sys.setrecursionlimit(100000)

box = list() #입력받은 리스트 저장
visited = list() #방문 체크 리스트
num = int(input()) #?x?리스트 인지

for _ in range(num): #리스트 입력
    box.append(list(input()))

for i in range(num): #방문체크리스트 초기화
    visited.append(list())
    for _ in range(num):
        visited[i].append("0")


area = int()
area2 = int()


class dot: #점 클래스
    def __init__(self, x, y):
        self.x = x
        self.y = y


def nonezerodot(): #방문하지 않은 좌표를 반환하기 위한 함수
    for i in range(num):
        for j in range(num):
            if visited[i][j] == "0":
                temp = dot(i, j)
                return temp
    return 0

def check(): #모든 리스트를 반복하기위해
    for i in range(num):
        for j in range(num):
            if visited[i][j] == "0":
                return 1
    return 0


def solve(i: int, j: int):
    if visited[i][j] == "1": #방문한 좌표일 경우 바로 리턴
        return
    visited[i][j] = "1" #방문 체크
    for m, n in (-1, 0), (1, 0), (0, -1), (0, 1): #상하좌우 체크를 위한 반복문
        if num > i + m >= 0 and num > j + n >= 0: #리스트 내부일 경우
            if box[i+m][j+n] == box[i][j]: #다음좌표와 현재좌표의 색이 같을 경우
                solve(i+m, j+n) #재귀


while check():
    temp = nonezerodot()
    solve(temp.x, temp.y)
    area += 1

for i in range(num): #방문체크 리스트 초기화
    for j in range(num):
        visited[i][j] = "0"

for i in range(num): #리스트내의 R값을 G로 바꿈
    for j in range(num):
        if box[i][j] == "R":
            box[i][j] = "G"

while check():
    temp = nonezerodot()
    solve(temp.x, temp.y)
    area2 += 1

print(area, end=" ")
print(area2)