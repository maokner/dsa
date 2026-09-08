class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                item = board[row][col]
                if item != ".":
                    if item in rows[row]:
                        return False
                    rows[row].add(item)

                    if item in cols[col]:
                        return False
                    cols[col].add(item)

                    boxNum = 3 * (row // 3) + (col // 3)

                    if item in boxes[boxNum]:
                        return False
                    boxes[boxNum].add(item)
        return True
                    
            