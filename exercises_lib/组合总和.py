# 给定一个无重复元素的数组 candidates 和一个目标数 target
# ，找出 candidates 中所有可以使数字和为 target 的组合。
#  candidates 中的数字可以无限制重复被选取。
#  说明：
#  所有数字（包括 target）都是正整数。
#  解集不能包含重复的组合。
#  示例 1：
#  输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
#
#  示例 2：
#
#  输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#  提示：
#  1 <= candidates.length <= 30
#  1 <= candidates[i] <= 200
#  candidate 中的每个元素都是独一无二的。
#  1 <= target <= 500
#  Related Topics 数组 回溯算法
#  👍 1024 👎 0

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs_fomb(index: int, cur_list: List[int]):
            cur_sum = sum(cur_list)
            if cur_sum < target:
                for i in range(index, ln):
                    cur_list.append(candidates[i])
                    dfs_fomb(i, cur_list)
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
        dfs_fomb(0, cur_list)
        return ans


if __name__ == '__main__':
    candidates = [2,3,6,7]
    candidates = [2,3,5]
    candidates =[2,7,6,3,5,1]
    target = 9
    test = Solution()
    res = test.combinationSum(candidates, target)
    print(res)