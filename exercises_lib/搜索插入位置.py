# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
#  你可以假设数组中无重复元素。
#
#  示例 1:
#
#  输入: [1,3,5,6], 5
# 输出: 2
#
#
#  示例 2:
#
#  输入: [1,3,5,6], 2
# 输出: 1
#
#
#  示例 3:
#
#  输入: [1,3,5,6], 7
# 输出: 4
#
#
#  示例 4:
#
#  输入: [1,3,5,6], 0
# 输出: 0
#
#  Related Topics 数组 二分查找

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        l = 0
        r = n-1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                if mid + 1 < n and nums[mid+1] <= target:
                    l = mid +1
                # elif mid + 1 < n and nums[mid+1] > target:
                #     return mid + 1
                else:
                    return mid+1
            elif target < nums[mid]:
                if mid - 1 >= 0 and nums[mid-1] >= target:
                    r = mid - 1
                # elif mid - 1 >= 0 and nums[mid-1] < target:
                #     return mid-1
                else:
                    return mid


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [2,3]
    target = 1
    test = Solution()
    res = test.searchInsert(nums, target)
    print(res)