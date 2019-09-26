N, M = map(int, input().split())


class Unit:
    check = False
    value = 0

    def __init__(self, m: bool, i: int):
        self.check = m
        self.value = i


sequence = [Unit(False, 0)]
result = [0] * M

for i in list(map(int, input().split())):
    sequence.append(Unit(False, i))


def makeSequence(i, n, m):
    if i == m:
        for k in range(m):
            print(result[k], end=' ')
        print()
        return
    for k in range(1, n + 1):
        if sequence[k].check:
            continue
        sequence[k].check = True
        result[i] = sequence[k].value
        makeSequence(i + 1, n, m)
        sequence[k].check = False


makeSequence(0, N, M)
