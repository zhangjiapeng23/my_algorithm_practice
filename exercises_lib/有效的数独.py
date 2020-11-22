# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
#  数字 1-9 在每一行只能出现一次。
#  数字 1-9 在每一列只能出现一次。
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#  上图是一个部分填充的有效的数独。
#
#  数独部分空格内已填入了数字，空白格用 '.' 表示。
#
#  示例 1:
#  输入:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: true
#
#  示例 2:
#  输入:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: false
# 解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
#      但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
#  说明:
#  一个有效的数独（部分已被填充）不一定是可解的。
#  只需要根据以上规则，验证已经填入的数字是否有效即可。
#  给定数独序列只包含数字 1-9 和字符 '.' 。
#  给定数独永远是 9x9 形式的。
#  Related Topics 哈希表


from typing import List

class Solution:
    def isValidSudoku_myself(self, board: List[List[str]]) -> bool:
        rows = 9
        cols = 9
        # 先 遍历检查行
        for row in range(rows):
            digit_set = set()
            for col in range(cols):
                if board[row][col].isdigit():
                    if board[row][col] not in digit_set:
                        digit_set.add(board[row][col])
                    else:
                        return False
                else:
                    continue
        # 再 遍历检查列
        for col in range(cols):
            digit_set = set()
            for row in range(rows):
                if board[row][col].isdigit():
                    if board[row][col] not in digit_set:
                        digit_set.add(board[row][col])
                    else:
                        return False
                else:
                    continue

        # 最后检查区域
        start_position = [[1, 1], [1, 4], [1, 7],
                          [4, 1], [4, 4], [4, 7],
                          [7, 1], [7, 4], [7, 7]]
        for p in start_position:
            digit_set = set()
            for x in range(-1, 2):
                for y in range(-1, 2):
                    num = board[p[0]+x][p[1]+y]
                    if num.isdigit():
                        if num not in digit_set:
                            digit_set.add(num)
                        else:
                            return False
                    else:
                        continue

        return True


    def is_vaild_sudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxs = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                boxs_index = (i // 3) * 3 + j // 3
                if num.isdigit():
                    num = int(num)
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxs[boxs_index][num] = boxs[boxs_index].get(num, 0) + 1

                    if rows[i][num] > 1 or cols[j][num] > 1 or boxs[boxs_index][num] > 1:
                        return False
        return True





if __name__ == '__main__':
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    test = Solution()
    res = test.isValidSudoku_myself(board)
    res2 = test.is_vaild_sudoku(board)
    print(res)
    print(res2)
