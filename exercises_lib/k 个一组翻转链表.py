# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
#  k 是一个正整数，它的值小于或等于链表的长度。
#
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#  示例：
#
#  给你这个链表：1->2->3->4->5
#
#  当 k = 2 时，应当返回: 2->1->4->3->5
#
#  当 k = 3 时，应当返回: 3->2->1->4->5
#  说明：
#  你的算法只能使用常数的额外空间。
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#  Related Topics 链表




# Definition for singly-linked list.
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            next = tail.next
            head, tail = self.reverse_listnode(head, tail)
            pre.next = head
            tail.next = next
            pre = tail
            head = tail.next

        return hair.next

    def reverse_listnode(self, head: ListNode, tail: ListNode) -> ListNode:
        prev = tail.next
        p = head
        while tail != prev:
            next = p.next
            p.next = prev
            prev = p
            p = next
        return tail, head


if __name__ == '__main__':
    nodes = []
    for i in range(1, 7):
        node = ListNode(val=i)
        nodes.append(node)

    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[4]

    head1 = nodes[0]
    temp = copy.deepcopy(head1)

    while temp:
        print(temp.val, end='->')
        temp = temp.next
    print()

    test = Solution()
    res = test.reverseKGroup(head1, 2)

    while res:
        print(res.val, end='->')
        res = res.next
    print()