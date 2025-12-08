from typing import List

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition

class VerboseSolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board is a 9x9 matrix representing a sudoku board.
        # Our goal is to determine if the board is valid.

        # First, I'll check each row to make sure each number 
        # is only represented once.
        
        for row in board:
            uniq = set()
            for col in row:
                if col == ".":
                    continue
                
                # Each row can only have 1 digit in the set {0,9}
                if col in uniq:
                    return False
                
                uniq.add(col)
        
        # Next, I'll check each col to make sure each number is only used once

        i = 0 # row
        j = 0 # col

        uniq = [set() for _ in range(9)]
        while i < 9 and j < 9:
            if board[i][j] != "." and board[i][j] in uniq[j]:
                print(f"{board[i][j]} exists twice in col {j}")
                return False
            
            uniq[j].add(board[i][j])

            if i == 8:
                j += 1
            i = (i + 1) % 9

        # Finally, I'll check each 3x3 grid within the 9x9 to
        # make sure each digit is unique

        i = 0 # row
        j = 0 # col
        uniq_3x3 = [set() for _ in range(9)]
        while i < 9 and j < 9:
            # Fetch the set that represents the grid i,j

            # Calculate the (row,col) index of the 3x3 grid that (i,j) falls in
            row_box = i // 3 # floor divide
            col_box = j // 3

            # Calculate the single (linear) index from [0,8] that (row,col) falls into
            # Use row-major linearization
            # index = row * number_of_columns + column
            index = row_box * 3 + col_box

            if board[i][j] != "." and board[i][j] in uniq_3x3[index]:
                print(f"{board[i][j]} exists twice in the {index} 3x3 grid")
                return False
            uniq_3x3[index].add(board[i][j])

            if i == 8:
                j += 1
            i = (i + 1) % 9
            
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board is a 9x9 matrix representing a sudoku board.
        # Our goal is to determine if the board is valid.

        i = 0 # row
        j = 0 # col
        uniq_row = [set() for _ in range(9)]
        uniq_col = [set() for _ in range(9)]
        uniq_3x3 = [set() for _ in range(9)]
        while i < 9 and j < 9:
            # Unique (i,j) within row i:
            if board[i][j] != "." and board[i][j] in uniq_row[i]:
                print(f"{board[i][j]} exists twice in row {i}")
                return False
            uniq_row[i].add(board[i][j])

            # Unique (i,j) within col j:
            if board[i][j] != "." and board[i][j] in uniq_col[j]:
                print(f"{board[i][j]} exists twice in col {j}")
                return False
            uniq_col[j].add(board[i][j])

            # Unique (i,j) within 3x3 check:
            # Calculate the (row,col) index of the 3x3 grid that (i,j) falls in
            row_box = i // 3 # floor divide
            col_box = j // 3

            # Calculate the single (linear) index from [0,8] that (row,col) falls into
            # Use row-major linearization
            # index = row * number_of_columns + column
            index = row_box * 3 + col_box

            if board[i][j] != "." and board[i][j] in uniq_3x3[index]:
                print(f"{board[i][j]} exists twice in the {index} 3x3 grid")
                return False
            uniq_3x3[index].add(board[i][j])

            if i == 8:
                j += 1
            i = (i + 1) % 9
            
        return True

                
valid_board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

invalid_board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

s = Solution()
# is_valid = s.isValidSudoku(valid_board)
is_valid = s.isValidSudoku(invalid_board)

print(is_valid)
