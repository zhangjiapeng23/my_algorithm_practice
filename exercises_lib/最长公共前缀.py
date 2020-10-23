"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明: 所有输入只包含小写字母 a-z 。
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 纵向比较， 依次比较每个字符串的相同位置的字符是否相同， 有不同则立即返回结果
        common_prefix = ''
        if len(strs) == 0:
            return ''
        min_str = min(len(s) for s in strs)
        for point in range(min_str):
            prefix = strs[0][point]
            for str_ in strs:
                if prefix == str_[point]:
                    continue
                else:
                    return common_prefix
            else:
                common_prefix += prefix
        else:
            return common_prefix

    def longest_common_prefix(self, strs: List[str]) -> str:
        # 横向比较，先两个相比较， 得出最长前缀，在和后面的比较，直到比到最后一个得出最长前缀，
        # 任意一次比较得到了空， 则直接返回结果为空
        if len(strs) == 0:
            return ''
        common_pre = strs[0]
        n = len(strs)
        for i in range(1,n):
            temp_pre = ''
            for point in range(min(len(common_pre), len(strs[i]))):
                if common_pre[point] == strs[i][point]:
                    temp_pre += common_pre[point]
                else:
                    break
            common_pre = temp_pre
            if common_pre == '':
                return common_pre
        return common_pre

    def longest_common_prefix_partition(self, strs: List[str]) -> str:
        # 分治的方法处理每个子问题
        def lcp(left: int, right: int) -> str:
            if left == right:
                return strs[left]
            middle = (left + right)//2
            left_str, right_str = lcp(left, middle), lcp(middle+1, right)
            min_len = min(len(left_str), len(right_str))
            for i in range(min_len):
                if left_str[i] != right_str[i]:
                    return left_str[:i]
            return left_str[:min_len]

        return '' if not strs else lcp(0, len(strs)-1)


    def longest_common_prefix_binary(self, strs: List[str]) -> str:
        # 二分查找，利用前缀的最长长度是有序的序列，从而进行折半查找
        def is_comom_prefix(length: int) ->bool:
            str0, count = strs[0][:length], len(strs)
            if all(strs[i][:length] == str0 for i in range(1, count)):
                return True

        low = 0
        high = min(len(s) for s in strs)
        while low < high:
            middle = (high - low + 1) // 2 + low
            if is_comom_prefix(middle):
                low = middle
            else:
                high = middle - 1

        return strs[0][:low]











if __name__ == '__main__':
    strs = ['abd', 'abc', 'ab']
    test = Solution()
    res = test.longestCommonPrefix(strs)
    res_1 = test.longest_common_prefix(strs)
    res_2 = test.longest_common_prefix_partition(strs)
    res_3 = test.longest_common_prefix_binary(strs)
    print(res, '\n'+res_1, '\n'+res_2, '\n'+res_3)