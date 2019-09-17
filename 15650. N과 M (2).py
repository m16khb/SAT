N, M = map(int, input().split())

sequence = [False] * (N + 1)
result = [0] * M


def makeSequence(i, n, m):
    if i == m:
        asc = True
        for k in range(len(result) - 1):
            if result[k] > result[k + 1]:
                asc = False
        if asc:
            for k in range(m):
                print(result[k], end=' ')
            print()
        return
    for k in range(1, n + 1):
        if sequence[k]:
            continue
        sequence[k] = True
        result[i] = k
        makeSequence(i + 1, n, m)
        sequence[k] = False


makeSequence(0, N, M)
