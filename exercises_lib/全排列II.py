# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
#
#  示例 2：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 8
#  -10 <= nums[i] <= 10
#
#  Related Topics 回溯算法
#  👍 531 👎 0

from typing import List


class Solution:

    def permuteUnique_self(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        _res = []

        def back_track(first, _nums, _res):
            if first < n:
                record_num = set()
                for i in range(first, n):

                    if _nums[i] in record_num:
                        continue
                    else:
                        _res.append(_nums[i])
                        record_num.add(_nums[i])
                        _nums[first], _nums[i] = _nums[i], _nums[first]
                        back_track(first+1, _nums, _res)
                        _nums[first], _nums[i] = _nums[i], _nums[first]
                        _res.pop()
            else:
                res.append(_res[:])

        back_track(0, nums, _res)
        return res


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def back_track(first):
            if first == n:
                return res.append(nums[:])
            else:
                record = set()
                for i in range(first, n):
                    if nums[i] in record:
                        continue
                    else:
                        record.add(nums[i])
                        nums[i], nums[first] = nums[first], nums[i]
                        back_track(first+1)
                        nums[i], nums[first] = nums[first], nums[i]

        back_track(0)
        return res




# if __name__ == '__main__':
#     nums = [1, 1, 2]
#     test = Solution()
#     ans = test.permuteUnique_self(nums)
#     ans1 = test.permuteUnique(nums)
#     print(ans)
#     print(ans1)
