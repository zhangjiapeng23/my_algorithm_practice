# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
#  示例:
#
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#  Related Topics 回溯算法
#  👍 1007 👎 0

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        res_temp = []
        n = len(nums)

        def dfs_premute(_res, i):
            if i < n:
                for num in nums:
                    if num not in _res:
                        _res.append(num)
                        dfs_premute(_res, i+1)
                        _res.pop()

            else:
                res.append(_res[:])

        dfs_premute(res_temp, 0)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    test = Solution()
    ans = test.permute(nums)
    print(ans)