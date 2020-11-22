# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
#
#
#
#  示例 1:
#
#  输入: [1,2,0]
# 输出: 3
#
#
#  示例 2:
#
#  输入: [3,4,-1,1]
# 输出: 2
#
#
#  示例 3:
#
#  输入: [7,8,9,11,12]
# 输出: 1
#
#
#
#
#  提示：
#
#  你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
#  Related Topics 数组
#  👍 834 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # 易错点： 下面的值的互换会导致出错，因为num[i]的值会先改变，
                # 从而第二数的坐标 nums[i]-1 会变化
                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]

                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for j in range(n):
            if nums[j] != j+1:
                return j+1
        return n+1



# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    nums = [2,7,8,9,11,12]
    test = Solution()
    res =test.firstMissingPositive(nums)
    print(res)


