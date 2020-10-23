# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#  示例:
#  给定 1->2->3->4, 你应该返回 2->1->4->3.


# Definition for singly-linked list.
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swap_pairs_recursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first_node = head
        second_node = head.next
        # swap pairs
        first_node.next = self.swap_pairs_recursive(second_node.next)
        second_node.next = first_node
        return second_node

    def swap_pairs_iter(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first_node = head
            seconde_node = head.next

            prev.next = seconde_node
            first_node.next = seconde_node.next
            seconde_node.next = first_node

            prev = first_node
            head = first_node.next
        return dummy.next




if __name__ == '__main__':
    nodes = []
    for i in range(1, 7):
        node = ListNode(val=i)
        nodes.append(node)

    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[4]

    head = nodes[0]
    head2 = copy.deepcopy(head)


    test = Solution()
    res = test.swap_pairs_recursive(head)
    res2 = test.swap_pairs_iter(head2)

    while res:
        print(res.val, end='->')
        res = res.next
    print()

    while res2:
        print(res2.val, end='->')
        res2 = res2.next
    print()



