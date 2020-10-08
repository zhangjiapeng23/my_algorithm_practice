"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 利用递归回溯来遍历所有的组合
        digits_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                      '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []
        _ans = []
        n = len(digits)
        if not digits:
            return list()

        def backtrack(_ans: List, index: int):
            if index == n:
                ans.append(''.join(_ans))
            else:
                for digit in digits_map[digits[index]]:
                    _ans.append(digit)
                    backtrack(_ans, index+1)
                    _ans.pop()

        backtrack(_ans, 0)
        return ans

    def letter_combinations(self, digits: str) -> List[str]:
        # 利用队列来循环遍历所有解
        digits_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                      '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        queue = ['']

        for digit in digits:
            for _ in range(len(queue)):
                temp = queue.pop(0)
                for letter in digits_map[digit]:
                    queue.append(temp + letter)
        return queue



if __name__ == '__main__':
    digits = '23'
    test = Solution()
    res = test.letterCombinations(digits)
    res1 = test.letter_combinations(digits)
    print(res)
    print(res1)