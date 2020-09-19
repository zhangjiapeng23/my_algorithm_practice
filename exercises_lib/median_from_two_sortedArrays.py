"""
给定两个大小为 m 和 n 的正序（从小到大）数组nums1 和nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设nums1和nums2不会同时为空。

来源：力扣（LeetCode）
"""
from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums = nums1
        le_nums = len(nums)
        self.quick_sort(nums, 0, le_nums-1)
        print(nums1)
        if le_nums % 2 == 0:
            median_num = (nums[le_nums//2] + nums[le_nums//2-1])/2
        else:
            median_num = nums[(le_nums+1)//2-1]

        return median_num





    def quick_sort(self, list1: List[int], left: int, right: int) -> int:
        if left < right:
            middle = self.middle_find(list1, left, right)
            self.quick_sort(list1, left, middle-1)
            self.quick_sort(list1, middle+1, right)
        else:
            return


    def middle_find(self, list1: List[int], left: int, right: int) -> int:
        midde = list1[left]
        while left < right:
            while left < right and list1[right] >= midde:
                right -= 1
            list1[left] = list1[right]
            while left < right and list1[left] <= midde:
                left += 1
            list1[right] = list1[left]

        list1[left] = midde

        return right






if __name__ == '__main__':
    l1 = [1,9,10,12]
    l2 = [3,4,8]
    tester = Solution()
    res = tester.findMedianSortedArrays(l1, l2)
    print(res)

