import numpy as np
from collections import deque
# piece = input()
grid = input().split()
matrix = deque()
for i in range(int(grid[1])):
    rows = []
    for j in range(int(grid[0])):
        rows.append('-')
    matrix.append(rows)

O = deque([[4, 14, 15, 5]])
I = deque([[4, 14, 24, 34], [3, 4, 5, 6]])
S = deque([[5, 4, 14, 13], [4, 14, 15, 25]])
Z = deque([[4, 5, 15, 16], [5, 15, 14, 24]])
L = deque([[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]])
J = deque([[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]])
T = deque([[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]])



def newgrid(current_state):
    # global matrix
    for index in current_state:
        if index < 10:
            index = '0' + str(index)
            matrix[int(index[0])][int(index[1])] = 0 if matrix[int(index[0])][int(index[1])] == '-' else '-'
        elif index > 99:
            index = str(index)
            matrix[int(index[0] + index[1])][int(index[2])] = 0 if matrix[int(index[0] + index[1])][int(index[2])] == '-' else '-'
        else:
            index = str(index)
            matrix[int(index[0])][int(index[1])] = 0 if matrix[int(index[0])][int(index[1])] == '-' else '-'


def static_obj_check(current_state):
    for index in current_state:
        if index < 10:
            index = '0' + str(index)
            if matrix[int(index[0])][int(index[1])] == '0':
                return True
        elif index > 99:
            index = str(index)
            if matrix[int(index[0] + index[1])][int(index[2])] == '0':
                return True
        else:
            index = str(index)
            if matrix[int(index[0])][int(index[1])] == '0':
                return True

def replace_piecestate():
    global piece
    piece = deque(piece)
    current_state= piece.popleft()
    new_state = piece[0]
    newgrid(new_state)

    piece.append(current_state)
    printgrid(matrix)
    newgrid(new_state)

def printgrid(matrix):
    for i in range(len(matrix)):
        # i.clear()
        for j in range(len(matrix[i])):
            matrix[i][j] = str(matrix[i][j])
        print(' '.join(matrix[i]))
    print('')

def grid_allocate():
    global current_state
    newgrid(current_state)
    printgrid(matrix)

printgrid(matrix)

while True:
        temp = []
        for i in range(int(grid[0])):
            temp_1 =[]
            for j in range(int(grid[1])):
                temp_1.append(True if matrix[j][i] == '0' else False)
            temp.append(all(temp_1))
        if any(temp):
            print('Game Over!')
            break
        action = input()

        if action == 'piece':
            piece = eval(input())
            current_state = piece[0]
            grid_allocate()
            newgrid(current_state)
        condition_1 = any([True if int(i) > int(grid[1] + '0') - 10 else False for i in current_state])
        piece = np.array(piece)

        if action == 'rotate':
            if not condition_1:
                piece += 10
                current_state = piece[0]
                if not static_obj_check(current_state):
                    replace_piecestate()
                else: piece -= 10
            else:
                grid_allocate()

        elif action == 'down':
            if not condition_1:
                piece += 10
                current_state = piece[0]
                if not static_obj_check(current_state):
                    grid_allocate()
                    newgrid(current_state)
                else:
                    piece -= 10
                    grid_allocate()
            else:
                piece -= 10
                grid_allocate()

        elif action == 'right':
            if not (any([True if str(i)[-1] == '9' else False for i in current_state]) or condition_1) :
                piece += 11
                current_state = piece[0]
                if not static_obj_check(current_state):
                    grid_allocate()
                    newgrid(current_state)
                else:
                    piece -= 11
                    grid_allocate()

            elif not condition_1:
                piece += 10
                current_state = piece[0]
                if not static_obj_check(current_state):
                    grid_allocate()
                    newgrid(current_state)
                else:
                    piece -= 10
                    grid_allocate()
            else:
                grid_allocate()

        elif action == 'left':
            # current_state = piece[0]
            if not (any([True if str(i)[-1] == '0' else False for i in current_state]) or condition_1):
                piece += 9
                current_state = piece[0]
                if not static_obj_check(current_state):
                    grid_allocate()
                    newgrid(current_state)
                else:
                    piece -= 9
                    grid_allocate()
            elif not condition_1:
                piece += 10
                current_state = piece[0]
                if not static_obj_check(current_state):
                    grid_allocate()
                    newgrid(current_state)
                else:
                    piece -= 10
                    grid_allocate()
            else:
                grid_allocate()

        elif action == 'break':
            while True:
                if all([True if matrix[int(grid[1]) - 1][i] == '0' else False for i in range(int(grid[0]))]):
                    matrix.pop()
                    matrix.appendleft(['-' for i in range(int(grid[0]))])
                    continue
                printgrid(matrix)
                break
        elif action == 'exit':
            break

