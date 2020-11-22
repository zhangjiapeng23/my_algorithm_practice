# 给定一个数组 candidates 和一个目标数 target ，
# 找出 candidates 中所有可以使数字和为 target 的组合。
#
#  candidates 中的每个数字在每个组合中只能使用一次。
#
#  说明：
#
#
#  所有数字（包括目标数）都是正整数。
#  解集不能包含重复的组合。
#
#
#  示例 1:
#
#  输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
#
#  示例 2:
#
#  输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]
#  Related Topics 数组 回溯算法
#  👍 430 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs_fomb(index: int, cur_list: List[int]):
            cur_sum = sum(cur_list)
            if cur_sum < target:
                for i in range(index, ln):
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                    cur_list.append(candidates[i])
                    dfs_fomb(i+1, cur_list)
                    cur_list.pop()
                return

            elif cur_sum == target:
                _ans = cur_list.copy()
                ans.append(_ans)
                return
            elif cur_sum > target:
                return

        cur_list = []
        ln = len(candidates)
        candidates.sort()
        dfs_fomb(0, cur_list)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    test = Solution()
    ans = test.combinationSum2(candidates, target)
    print(ans)