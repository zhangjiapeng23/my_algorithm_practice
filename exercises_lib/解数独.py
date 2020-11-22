# 编写一个程序，通过填充空格来解决数独问题。
#  一个数独的解法需遵循如下规则：
#  数字 1-9 在每一行只能出现一次。
#  数字 1-9 在每一列只能出现一次。
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#  空白格用 '.' 表示。
#  一个数独。
#  答案被标成红色。
#
#  提示：
#
#
#  给定的数独序列只包含数字 1-9 和字符 '.' 。
#  你可以假设给定的数独只有唯一解。
#  给定数独永远是 9x9 形式的。
#
#  Related Topics 哈希表 回溯算法

# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".","4",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8","5","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".","3",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(pos: int):
            if pos == len(space):
                return True

            i, j = space[pos]
            box_index = (i // 3) * 3 + j // 3
            for num_str in range(1, 10):
                if rows[i].get(num_str, 0) < 1 and cols[j].get(num_str, 0) < 1 and boxs[box_index].get(num_str, 0) < 1:
                    board[i][j] = str(num_str)
                    rows[i][num_str] = rows[i].get(num_str, 0) + 1
                    cols[j][num_str] = cols[j].get(num_str, 0) + 1
                    boxs[box_index][num_str] = boxs[box_index].get(num_str, 0) + 1
                    res = dfs(pos + 1)
                    if res is False:
                        board[i][j] = '.'
                        rows[i][num_str] = rows[i][num_str] - 1
                        cols[j][num_str] = cols[j][num_str] - 1
                        boxs[box_index][num_str] = boxs[box_index][num_str] - 1
                    else:
                        break
            else:
                return False

        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxs = [{} for _ in range(9)]
        space = []

        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    box_index = (i // 3) * 3 + j // 3
                    num = int(board[i][j])
                    rows[i][num] = 1
                    cols[j][num] = 1
                    boxs[box_index][num] = 1
                else:
                    space.append((i, j))


        dfs(0)