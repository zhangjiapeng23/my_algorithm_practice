"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nds = []
        nd = head
        while nd:
            nds.append(nd)
            nd = nd.next
        if len(nds) == 1:
            return None
        if n == len(nds):
            head = nds[1]
        elif n == 1:
            nds[-2].next = None
        else:
            nds[-n - 1].next = nds[-n + 1]
        return head

    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        length = 0
        dummy.next = head
        first = head
        while first is not None:
            length +=1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next



if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    n = 3
    # nums = [1]
    # n = 1
    nds = []
    for i in nums:
        node = ListNode(val=i)
        nds.append(node)
    for j in range(len(nds) - 1):
        nds[j].next = nds[j + 1]
    head = nds[0]

    temp = head
    while temp:
        print(temp.val, end=' ')
        temp = temp.next
    else:
        print()

    test = Solution()
    # res = test.removeNthFromEnd(head, n)
    res = test.remove_nth_from_end(head, n)

    while res:
        print(res.val, end=' ')
        res = res.next
