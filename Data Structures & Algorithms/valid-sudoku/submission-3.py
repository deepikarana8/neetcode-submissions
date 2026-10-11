class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # def helper(x, y):
        #     if board[x][y] in box_set:
        #         return False
        #     else:
        #         if board[x][y] != ".":
        #             box_set.add(board[x][y])
        #     print(box_set, "1", board[x][y])
                
        # check columns
        for c in range(len(board)):
            col_set = set()
            for r in range(len(board[0])):
                if board[r][c] in col_set:
                    return False
                else:
                    if board[r][c] != ".":
                        col_set.add(board[r][c])

        # check rows
        for r in range(len(board[0])):
            row_set = set()
            for c in range(len(board)):
                if board[r][c] in row_set:
                    return False
                else:
                    if board[r][c] != ".":
                        row_set.add(board[r][c])

        # check 3x3 box for repetition
        for r in range(0, len(board), 3):
            for c in range(0, len(board[0]), 3):
                box_set = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        num = board[i][j]
                        if num == ".":
                            continue
                        if num in box_set:
                            return False
                        box_set.add(num)
                        # this is NOT n^4 runtime, because this runs a set amount of 3 times. It's quanitifable and not dependent. it's 3 times each time, so it counts as a constant. thus, runtime is n^2 + 3n --> n^2



        # for r in range(0, len(board), 3):
        #     for c in range(0, len(board[0]), 3):
        #         box_set = set()
        #         helper(r, c)
        #         helper(r+1, c)
        #         helper(r+2, c)
        #         helper(r, c+1)
        #         helper(r+1, c+1)
        #         helper(r+2, c+1)
        #         helper(r, c+2)
        #         helper(r+1, c+2)
        #         helper(r+2, c+2)
        
        return True

    
        

        