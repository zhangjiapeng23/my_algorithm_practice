"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            _height = min(height[left], height[right])
            _weight = right - left
            max_area = max(max_area, _height*_weight)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    test = Solution()
    res = test.maxArea(height)
    print(res)