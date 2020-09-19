"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for index in range(len(s)):
            substring = s[index]
            for _index in range(index+1, len(s)):
                if s[_index] not in substring:
                    substring += s[_index]
                else:
                    max_length = max_length if max_length > len(substring) else len(substring)
                    break
            else:
                max_length = max_length if max_length > len(substring) else len(substring)

        return max_length

    def lengthOfLongestSubstring_better(self, s: str) -> int:
        # 利用滑动窗口来记录最长子串
        l_max = 0
        ln = len(s)
        substr_set = set()
        right = -1
        for i in range(ln):
            if i != 0:
                # 左指针向右移动一位
                substr_set.remove(s[i-1])
            while right+1 < ln and s[right+1] not in substr_set:
                # 右指针向右移动一位
                substr_set.add(s[right+1])
                right +=1
            l_max = max(l_max, right+1 - i)
        return l_max




if __name__ == '__main__':
    s = 'abdaaildd'
    tester = Solution()
    # res = tester.lengthOfLongestSubstring(s)
    res = tester.lengthOfLongestSubstring_better(s)
    print(res)