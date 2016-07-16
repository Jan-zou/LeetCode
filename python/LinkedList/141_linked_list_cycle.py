# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a linked list, determine if it has a cycle in it.
    Follow up: Can you solve it without using extra space?

Tags: Linked List, Two Pointers
O(n) runtime; O(1) space
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # two pointers - slow慢指针, 一次走一步; fast快指针, 一次走两步; 如果有循环则快慢指针一定会在某一时刻遇上
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
