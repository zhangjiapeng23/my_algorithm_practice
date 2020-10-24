# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# （更大的排列就是指列表各个位置的数组成一个比当前位置的数更大的一个排列）
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#  必须原地修改，只允许使用额外常数空间。
#  以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#  Related Topics 数组


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        point = n-1
        # 从列表尾部向前遍历找到前一个位置小于后一个位置的point
        while point > 0:
            if nums[point] <= nums[point-1]:
                point -= 1
            else:
                break

        # 从找到的point向后找到一个最小的比他大位置进行交换
        temp_p = point
        while 0 < temp_p < n - 1:
            if nums[point-1] < nums[temp_p] and nums[point-1] < nums[temp_p+1]:
                temp_p += 1
            else:
                nums[temp_p], nums[point - 1] = nums[point - 1], nums[temp_p]
                break
        else:
            nums[n-1], nums[point - 1] = nums[point - 1], nums[n-1]

        # 交换后，将point的位置后面的进行升序排列 (reverse)
        i = point
        j = n-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    a = [1, 2, 3]
    a = [3, 2, 1]
    a = [1, 1, 5]
    a = [1, 3, 2]
    # a = [2, 3, 1]
    test = Solution()
    test.nextPermutation(a)
    print(a)

