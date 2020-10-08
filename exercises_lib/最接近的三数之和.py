"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 
提示：
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = None
        min_gap = None
        n = len(nums)
        nums.sort()
        for i in range(n):
            left, right = i+1, n-1
            while left < right:
                gap = target - (nums[i] + nums[left] + nums[right])
                if min_gap is None or min_gap > abs(gap):
                    min_gap = abs(gap)
                    ans = nums[i] + nums[left] + nums[right]
                if nums[i] + nums[left] + nums[right] > target:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    return nums[i] + nums[left] + nums[right]


        return ans


if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 1
    test = Solution()
    res = test.threeSumClosest(nums, target)
    print(res)


