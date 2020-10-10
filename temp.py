import random
from typing import List


def insert_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(1, n):
        temp = nums[i]
        while i-1 >= 0 and nums[i-1] > temp:
            nums[i] = nums[i-1]
            i -= 1
        nums[i] = temp

    return nums

def select_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n):
        max_index = 0
        for j in range(n-i):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[j], nums[max_index] = nums[max_index], nums[j]
    return nums

def bubble_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def quick_sort(nums: List[int], left: int, right: int) -> int:
    if left < right:
        middle = partition(nums, left, right)
        quick_sort(nums, left, middle-1)
        quick_sort(nums, middle+1, right)


def partition(nums: List[int], left: int, right: int) -> int:
    middle = nums[left]
    while left < right:
        while left < right and nums[right] >= middle:
            right -=1
        nums[left] = nums[right]
        while left < right and nums[left] <= middle:
            left +=1
        nums[right] = nums[left]
    nums[left] = middle
    return left




if __name__ == '__main__':
    nums = [x for x in range(100)]
    nums1, nums2, nums3, nums4 = nums, nums, nums, nums
    random.shuffle(nums1)
    random.shuffle(nums2)
    random.shuffle(nums3)
    random.shuffle(nums4)
    print(nums1)
    print(nums2)
    print(nums3)
    print(nums4)
    res = insert_sort(nums1)
    res1 = select_sort(nums2)
    res2 = bubble_sort(nums3)
    quick_sort(nums4, 0, len(nums)-1)
    print(res)
    print(res1)
    print(res2)
    print(nums4)