num = int(input())
result = list()
result.append(1)
result.append(1)
# 초기값 설정


def solve(index: int): #점화식을 세워 미리 배열에 저장하여 계산을 줄임
    result.append(result[index - 1] + result[index - 2])


for i in range(2, num + 1):
    solve(i)

print(result[num] % 10007)
