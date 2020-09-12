"""
给定一个整数数组 num 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


"""
from typing import List


class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
       for index, num in enumerate(nums):
           count = index+1
           for _index, _num in enumerate(nums[index + 1:]):
               if num + _num == target:
                   return [index, _index + count]
               else:
                   count += 1
       else:
           return []

    def better_two_sum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            for _index in range(index+1, len(nums)):
                if nums[index] + nums[_index] == target:
                    return [index, _index]
        else:
            return []

    def best_two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        利用字典对已经遍历过的没匹配的num 进行存储， 从而节省遍历时间 只需一个for循环 时间是 O(n)
        :param nums:
        :param target:
        :return:
        """
        hash_map = {}
        for index in range(len(nums)):
            if hash_map.get(target-nums[index]) is not None:
                return [hash_map.get(target-nums[index]), index]
            else:
                hash_map[nums[index]] = index







"""
错误点：
target = 6
【3，3】【3，2，4】
（1）第二个循环的数字用了切片，得出的index是新数组的index。
（2）添加index的计数器时，初始化值要和第一循环的index关联上。

"""



if __name__ == '__main__':
    a = Solution()
    # res = a.two_sum([3,2,4], 6)
    res = a.better_two_sum([3, 2, 4], 6)
    print(res)
