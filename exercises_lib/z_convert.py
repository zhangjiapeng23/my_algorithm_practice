# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#  比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# L   C   I   R
# E T O E S I I G
# E   D   H   N
#  之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#  请你实现这个将字符串进行指定行数变换的函数：
#  string convert(string s, int numRows);
#  示例 1:
#  输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#  示例 2:
#  输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G


class Solution:

    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        col = []
        row = [None]*numRows
        point = 0
        row_point = 0
        if numRows == 1:
            return s

        for i in s:
            if point == 0:
                if row_point < numRows:
                    if row_point != 0:
                        row = col.pop()
                    row[row_point] = i
                    col.append(row)
                    row_point += 1
                    if row_point == numRows:
                        row_point = 0
                        point = (numRows-2)
                        row = [None] * numRows
            else:
                row[point] = i
                col.append(row)
                point -= 1
                row = [None] * numRows

        for k in range(numRows):
            for j in range(len(col)):
                if col[j][k] is not None:
                    ans += col[j][k]
        return ans

    def convert_best(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        flag = -1
        point = 0
        # 每一行的结果就是list的一个成员， list_1[0]为第一行，以此类推
        list_1 = ['' for _ in range(numRows)]
        for i in s:
            # 当遇到一行或者最后一行时，方向改变，flag取反
            if point == 0 or point == numRows-1:
                flag = -flag
            list_1[point] += i
            point += flag

        ans = "".join(list_1)

        return ans


if __name__ == '__main__':
    s = 'LEETCODEISHIRING'
    test = Solution()
    res = test.convert(s, 4)
    res_2 = test.convert_best(s, 4)
    print(res)
    print(res_2)

