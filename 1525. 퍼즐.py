# initial_form = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# puzzle = list()
# for _ in range(3):
#     puzzle.append(list(map(int, input().split())))
#
#
# def move(num: int, x: int, y: int):
#     for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
#         if x + i > 2 or y + j > 2 or x + i < 0 or y + j < 0:
#             continue
#         temp = initial_form[x][y]
#         initial_form[x][y] = initial_form[x + i][y + j]
#         initial_form[x + i][y + j] = temp
#         x = x + i
#         y = y + j
#         if initial_form == puzzle:
#             print(num)
#             break
#         else:
#             move(num + 1, x, y)
#
#
# move(1, 2, 2)
