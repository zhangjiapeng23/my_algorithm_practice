"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def merge_two_list(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                prev = prev.next
                l1 = l1.next
            else:
                prev.next = l2
                prev = prev.next
                l2 = l2.next
        prev.next = l1 if l1 is not None else l2
        return prehead.next




if __name__ == '__main__':
    nodes = []
    for i in range(1, 7):
        node = ListNode(val=i)
        nodes.append(node)

    nodes[0].next = nodes[2]
    nodes[2].next = nodes[5]
    nodes[1].next = nodes[3]
    nodes[3].next = nodes[4]

    temp = nodes[0]
    temp1 = nodes[1]

    while temp:
        print(temp.val, end='->')
        temp = temp.next
    print()

    while temp1:
        print(temp1.val, end='->')
        temp1 = temp1.next
    print()


    l1 = nodes[0]
    l2 = nodes[1]
    test = Solution()
    res = test.merge_two_list(l1, l2)

    while res:
        print(res.val, end='->')
        res = res.next



