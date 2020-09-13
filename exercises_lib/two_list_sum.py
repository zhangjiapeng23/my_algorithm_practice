"""
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0开头
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNoseGenerator:
    def __init__(self, vals):
        self.nodes = []
        self.list = None
        self.vals = vals
        for val in self.vals:
            self.nodes.append(ListNode(val))
        for index in range(len(vals)-1):
            self.nodes[index].next = self.nodes[index+1]
        if len(self.nodes) > 0:
            self.list = self.nodes[0]
        else:
            self.list = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodes_list = []
        carry = 0
        while l1 or l2 or carry:
            list_temp = ListNode(0)
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val

            temp_sum = l1_val + l2_val + carry
            if temp_sum < 10:
                list_temp.val = temp_sum
                carry = 0
            else:
                list_temp.val = temp_sum - 10
                carry = 1
            nodes_list.append(list_temp)
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        for index in range(len(nodes_list)-1):
            nodes_list[index].next = nodes_list[index+1]
        return nodes_list[0]


    def addTwoNumbers_better(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_head = ListNode(0)
        curr_node = list_head
        carry = 0
        while l1 or l2:
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            temp_sum = l1_val + l2_val + carry
            #整除，得到下一层的进位值
            carry = temp_sum // 10
            #取余获得当前侧的值
            curr_node.next = ListNode(temp_sum % 10)
            curr_node = curr_node.next
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        if carry > 0:
            curr_node.next = ListNode(carry)
        return list_head.next


"""
错误点"
当是[5], [5] 结果是[0, 1]时。
while 没有把carry的数值加进来判断，导致循环提前结束，得到了[0].

测试用例	说明
l1=[0,1]l1=[0,1]，l2=[0,1,2]l2=[0,1,2]	当一个列表比另一个列表长时
l1=[]l1=[]，l2=[0,1]l2=[0,1]	当一个列表为空时，即出现空列表
l1=[9,9]l1=[9,9]，l2=[1]l2=[1]	求和运算最后可能出现额外的进位，这一点很容易被遗忘

"""



if __name__ == '__main__':
    list_1 = ListNoseGenerator([1,2,4])
    list_2 = ListNoseGenerator([5,9])
    l1 = list_1.list
    l2 = list_2.list

    tester = Solution()
    # list_res = tester.addTwoNumbers(l1, l2)
    list_res = tester.addTwoNumbers_better(l1, l2)
    res = []
    while list_res:
        res.append(list_res.val)
        list_res = list_res.next

    print(res)
