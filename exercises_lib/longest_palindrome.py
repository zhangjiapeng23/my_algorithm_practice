# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
#  示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
#  示例 2：
#
#  输入: "cbbd"
# 输出: "bb"



# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 创建一个二维数组存储各个子串是否为回文的状态
        l_s = len(s)
        l_max = 0
        substr = ''
        dp = [[False]*l_s for _i in range(l_s)]
        # 枚举子串的长度为 l+1， 子串的末尾位置为 j =  i+l+1-1 = l+i
        for l in range(l_s):
            # 遍历每个子串的起始位置 i
            for i in range(l_s):
                j = i+l
                if j >= l_s:
                    break
                elif l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] is True and l+1 > l_max:
                    l_max = l
                    substr = s[i:j+1]
        return substr

# leetcode submit region end(Prohibit modification and deletion)


"""
错误分析：
使用动态规划，得出推导式和初始值：
对dp表进行填表时，应该按照枚举子串长度来遍历: l=1, 2, 3, 4...
而不是 从初始位置 i= 0，1，2... 子串末尾位置 j = 0, 1, 2.. 来遍历， 因为
这样会有前面参考的位置的状态还没有确定，导致后面的结果出错。
推导式：
当 l = 1, dp[i][j] = true i==j,
当 l = 2, dp[i][j] = s[i] == s[j]
当 l > 2, dp[i][j] = dp[i+1][j-1] and s[i] == s[j]

"""

if __name__ == '__main__':
    s = 'baabsbs'
    tester = Solution()
    res = tester.longestPalindrome(s)
    print(res)
