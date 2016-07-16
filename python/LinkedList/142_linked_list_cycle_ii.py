# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a linked list, return the node where the cycle begins.
    If there is no cycle, return null.

    Note: Do not modify the linked list.
    Follow up: Can you solve it without using extra space?

Tags: Linked List, Two Pointers
O(n) runtime; O(1) space

链表头head到环路起点步数为K, 从起点到相遇点步数为M, 环路长度为L
快、慢指针相遇时走的步数为:
    slow = K + M
    fast = K + M + nL
快指针每次走两步, 慢指针每次走一步:
    fast = 2 * slow
==> K + M = nL
因此，第一次相遇后，将快指针放置链表头head，慢指针仍在相遇点；当慢指针到环路起点时，快指针也到此处。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None
