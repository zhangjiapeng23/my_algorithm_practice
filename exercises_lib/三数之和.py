"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def is_same(nums1: List[int], nums2: List[int]) -> bool:
            for i in nums1:
                if i not in nums2:
                    return False
            else:
                for j in nums2:
                    if j not in nums1:
                        return False
                return True
        ans = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        for _ans in ans:
                            if is_same(_ans, [nums[i], nums[j], nums[k]]):
                                break
                        else:
                            ans.append([nums[i], nums[j], nums[k]])
        return ans

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            # 去重，连续位置如果值相同则跳过他
            if i == 0 or nums[i] != nums[i-1]:
                right = n - 1
                for j in range(i+1, n):
                    if j == i+1 or nums[j] != nums[j-1]:
                        while (j < right and nums[i] + nums[j] + nums[right] > 0):
                            right -= 1
                        # 去除因为 j == right， 跳出循环的情况。
                        if j == right:
                            break
                        if nums[i] + nums[j] + nums[right] == 0:
                            ans.append([nums[i], nums[j], nums[right]])
        return ans


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    test = Solution()
    res = test.threeSum(nums)
    res1 = test.three_sum(nums)
    print(res, '\n', res1)
