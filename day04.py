# Day 4: Giant Squid (Bingo)

import load_data as ld 

def split_instructions_and_boards(data):
    instructions = data[0]
    boards = []
    board = []
    for line in data[1:]: 
        if(len(line) > 0):
            numbers = line.split()
            board.append(numbers)
        if(len(board) == 5):
            boards.append(board)
            board = []
    if(len(board) > 0):
        boards.append(board)
    return instructions, boards

def check_row(board, row_idx):
    count = 0
    for col_idx in range(len(board)):
        if(board[row_idx][col_idx][0] == '-'):
            count += 1
    if(count == 5):
        return 1
    else:
        return 0

def check_column(board, col_idx):
    count = 0
    for row_idx in range(len(board)):
        if(board[row_idx][col_idx][0] == '-'):
            count += 1
    if(count == 5):
        return 1
    else:
        return 0

# def check_forward_diagonal(board):
#     count = 0
#     for row_idx in range(len(board)):
#         for col_idx in range(len(board)):
#             if(row_idx == col_idx):
#                 if(board[row_idx][col_idx][0] == '-'):
#                     count += 1
#     if(count == 5):
#         return 1
#     else:
#         return 0

# def check_backward_diagonal(board):
#     count = 0
#     for row_idx in range(len(board)):
#         for col_idx in range(len(board)):
#             if(row_idx + col_idx == 4):
#                 if(board[row_idx][col_idx][0] == '-'):
#                     count += 1
#     if(count == 5):
#         return 1
#     else:
#         return 0

def sum_board(board):
    sum = 0
    for row_idx in range(len(board)):
        for col_idx in range(len(board)):
            if(board[row_idx][col_idx][0] != '-'):
                sum += int(board[row_idx][col_idx])
    return sum 


def part1(instructions, boards):
    bingo = False
    for n in instructions.split(','):
        print(n)
        for board in boards:
            for col_idx, line in enumerate(board):
                for row_idx, nn in enumerate(line):
                    if(board[row_idx][col_idx] == n):
                        board[row_idx][col_idx] = '-' + n # changing it to negative to convey that it has been selected
                        bingo = check_row(board, row_idx)
                        if(bingo):
                            print(f'{n}? Bingo!')
                            print(board)
                            return sum_board(board) * int(n)
                        bingo = check_column(board, col_idx)
                        if(bingo):
                            print(f'{n}? Bingo!')
                            print(board)
                            return sum_board(board) * int(n)
                        # if(row_to_check == col_to_check):
                        #     bingo = check_forward_diagonal(board)
                        #     if(bingo):
                        #         print(f'{n}? Bingo!')
                        #         print(board)
                        #         return sum_board(board) * int(n)
                        # if(row_to_check + col_to_check == 4):
                        #     bingo = check_backward_diagonal(board)
                        #     if(bingo):
                        #         print(f'{n}? Bingo!')
                        #         print(board)
                        #         return sum_board(board) * int(n)
    print('End of instructions')
    return 0

def part2(instructions, boards):
    bingo_boards = []
    for n in instructions.split(','):
        print(n)
        for board in boards:
            for col_idx, line in enumerate(board):
                for row_idx, nn in enumerate(line):
                    if(board[row_idx][col_idx] == n):
                        board[row_idx][col_idx] = '-' + n # changing it to negative to convey that it has been selected
                        bingo = check_row(board, row_idx)
                        if(bingo):
                            print(f'{n}? Bingo!')
                            print(board)
                            # Add board to bingo_boards if it isn't already there
                            if board not in bingo_boards:
                                bingo_boards.append(board)
                            print(len(bingo_boards), len(boards))
                            # Check if length of bingo_boards = length of boards
                            if(len(bingo_boards) == len(boards)):
                                return sum_board(board) * int(n)
                        bingo = check_column(board, col_idx)
                        if(bingo):
                            print(f'{n}? Bingo!')
                            print(board)
                            if board not in bingo_boards:
                                bingo_boards.append(board)
                            print(len(bingo_boards), len(boards))
                            if(len(bingo_boards) == len(boards)):
                                return sum_board(board) * int(n)
    print('End of instructions')
    return 0

# data = ld.load_data('example04.txt')
data = ld.load_data('input04.txt')
instructions, boards = split_instructions_and_boards(data)
print(f'{part1(instructions, boards)}') # 10680
print(f'{part2(instructions, boards)}') # 31892 
