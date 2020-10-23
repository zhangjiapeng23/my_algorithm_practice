# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
#  示例 1:
#
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#
#
#  示例 2:
#
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#
#  Related Topics 字符串 动态规划




class Solution(object):
    def longestValidParentheses(self, s):
        ans = 0
        n = len(s)
        dp = [0 for _ in range(n)]
        pv = 1
        while pv < n:
            if s[pv] == '(':
                dp[pv] = 0
            else:
                if s[pv] == ')':
                    if s[pv-1] == '(':
                        if pv > 1:
                            dp[pv] = dp[pv-2] + 2
                        else:
                            dp[pv] = 2
                    elif pv - dp[pv-1] >0 and s[pv - dp[pv-1] -1] == '(':
                        if pv - dp[pv-1] -1 > 0:
                                dp[pv] = dp[pv-1] + dp[pv - dp[pv-1] -2] + 2
                        else:
                            dp[pv] = dp[pv-1] + 2

            ans = max(ans, dp[pv])
            pv += 1
        return ans


    def longestValidParentheses_2(self, s):
        ans =0
        n = len(s)
        stack = [-1]
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans






if __name__ == '__main__':
    s = ''
    test = Solution()
    res1 = test.longestValidParentheses(s)
    res = test.longestValidParentheses_2(s)
    print(res1)
    print(res)


