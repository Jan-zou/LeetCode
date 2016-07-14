# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Reverse a singly linked list.
    Hint:
        A linked list can be reversed either iteratively or recursively.
        Could you implement both?

Tags: Linked List

思路：
    不妨拿出四本书，摞成一摞（自上而下为 A B C D），要让这四本书的位置完全颠倒过来（即自上而下为 D C B A）：
    盯住书A，每次操作把A下面的那本书放到最上面
    初始位置：自上而下为 A B C D
    第一次操作后：自上而下为 B A C D
    第二次操作后：自上而下为 C B A D
    第三次操作后：自上而下为 D C B A
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    # iteratively - O(n) runtime; O(1) space
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next


    # recursively - O(n) runtime; O(n) space
    def reverseList2(self, head):
        [begin, end] = self.reverseListRecu(head)
        return begin

    def reverseListRecu(self, head):
        if not head:
            return [None, None]

        [begin, end] = self.reverseListRecu(head.next)

        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]

    def reverseList3(self, head):
        if not head or not head.next:
            return head

        p = self.reverseList3(head.next)
        head.next.next = head
        head.next = None
        return p

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().reverseList(head)
    print Solution().reverseList2(head)
    print Solution().reverseList3(head)
