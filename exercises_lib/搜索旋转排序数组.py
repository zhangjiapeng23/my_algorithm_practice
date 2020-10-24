# 给你一个升序排列的整数数组 nums ，和一个整数 target 。
#
#  假设按照升序排序的数组在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。
#
#  请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#  示例 1：
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#  示例 2：
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#  示例 3：
# 输入：nums = [1], target = 0
# 输出：-1
#  提示：
#  1 <= nums.length <= 5000
#  -10^4 <= nums[i] <= 10^4
#  nums 中的每个值都 独一无二
#  nums 肯定会在某个点上旋转
#  -10^4 <= target <= 10^4
#
#  Related Topics 数组 二分查找
from typing import List


class Solution(object):
    def search(self, nums: List[int], target: int) ->int:
        n = len(nums)
        ans = self.search_num(0, n-1, nums, target)
        return ans

    def search_num(self, left, right, nums, target):
        if left < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if left < mid and nums[left] <= nums[mid - 1]:
                if nums[left] <= target <= nums[mid-1]:
                    return self.search_num_sort(left, mid-1, nums, target)
                else:
                    return self.search_num(mid+1, right, nums, target)
            else:
                if nums[mid+1] <= target <= nums[right]:
                    return self.search_num_sort(mid+1, right, nums, target)
                else:
                    return self.search_num(left, mid-1, nums, target)
        else:
            if nums[left] == target:
                return left
            else:
                return -1

    def search_num_sort(self, left, right, nums, target):

        if left < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                return self.search_num_sort(left, mid-1, nums, target)
            else:
                return self.search_num_sort(mid+1, right, nums, target)
        else:
            if nums[left] == target:
                return left
            else:
                return -1


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [5, 1, 3]
    # nums = [1, 3]
    # nums = [3, 4, 1]
    # nums= [2,3,4,5,6,7,8,9,1]
    test = Solution()
    res = test.search(nums, 1)
    print(res)


