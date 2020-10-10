"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        valid_hash = {')': '(', ']': '[', '}': '{'}
        stack = []
        n = len(s)
        if s is None:
            return False
        if n % 2 == 1:
            return False
        for i in s:
            if i in valid_hash:
                if stack and valid_hash[i] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(i)

        return not stack

        # if valid_hash[s[0]] is None:
        #     stack.append(s[0])
        # else:
        #     return False
        # while stack:
        #     for i in range(1, n):
        #         if valid_hash[s[i]] is None:
        #             stack.append(s[i])
        #         else:
        #             if valid_hash[s[i]] == stack.pop():
        #                 continue
        #             else:
        #                 return False
        # return True




if __name__ == '__main__':
    s = '()[]{}'
    s = '{[]}'
    s = '([)]'
    s = '(]'
    s = ']'
    test = Solution()
    res = test.isValid(s)
    print(res)


