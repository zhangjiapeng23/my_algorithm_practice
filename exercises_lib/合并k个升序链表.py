# 给你一个链表数组，每个链表都已经按升序排列。
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。
#  示例 1：
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#  示例 2：
#  输入：lists = []
# 输出：[]
#  示例 3：
#  输入：lists = [[]]
# 输出：[]
#  提示：
#  k == lists.length
#  0 <= k <= 10^4
#  0 <= lists[i].length <= 500
#  -10^4 <= lists[i][j] <= 10^4
#  lists[i] 按 升序 排列
#  lists[i].length 的总和不超过 10^4

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)

        def merge_lists_divide(_list, left, right):
            if left == right:
                return _list[left]
            if left > right:
                return None
            mid = (left+right)//2
            return sort_lists(merge_lists_divide(_list, left, mid), merge_lists_divide(_list, mid+1, right))

        def sort_lists(node1: ListNode, node2: ListNode):
            prenode = ListNode(-1)
            prev = prenode
            while node1 and node2:
                if node1.val < node2.val:
                    prev.next = node1
                    node1 = node1.next
                else:
                    prev.next = node2
                    node2 = node2.next
                prev = prev.next
            prev.next = node1 if node1 is not None else node2
            return prenode.next

        res = merge_lists_divide(lists, 0, n-1)
        return res




if __name__ == '__main__':
    nodes = []
    nodes2 = []
    for i in range(1, 7):
        node = ListNode(val=i)
        nodes.append(node)

    for i in range(1, 7):
        node = ListNode(val=i)
        nodes2.append(node)

    nodes[0].next = nodes[2]
    nodes[2].next = nodes[5]
    nodes[1].next = nodes[3]
    nodes[3].next = nodes[4]

    nodes2[0].next = nodes2[2]
    nodes2[2].next = nodes2[5]
    nodes2[1].next = nodes2[3]
    nodes2[3].next = nodes2[4]

    temp = nodes[0]
    temp1 = nodes[1]
    temp2 = nodes2[0]

    test_list = [temp, temp1, temp2]
    while temp:
        print(temp.val, end='->')
        temp = temp.next
    print()
    while temp1:
        print(temp1.val, end='->')
        temp1 = temp1.next
    print()
    while temp2:
        print(temp2.val, end='->')
        temp2 = temp2.next
    print()

    test = Solution()
    res = test.mergeKLists(test_list)

    while res:
        print(res.val, end='->')
        res = res.next








