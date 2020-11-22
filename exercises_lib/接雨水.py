#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
#  提示：
#
#
#  n == height.length
#  0 <= n <= 3 * 104
#  0 <= height[i] <= 105
#
#  Related Topics 栈 数组 双指针

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        left_max = right_max = 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] <= left_max:
                    ans += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] <= right_max:
                    ans += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return ans


if __name__ == '__main__':
    height = [2, 1,2]
    test = Solution()
    ans = test.trap(height)
    print(ans)



