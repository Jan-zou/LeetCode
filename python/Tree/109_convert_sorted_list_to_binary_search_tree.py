# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Tags: Depth-first Search, Linked List

Linked list no longer have random access to an element in O(1) time.
Method 1: Brute force - O(nlogn) runtime, O(logn) stack space
    apply the same solution from Question "Convert Sorted Array to Balanced Binary Search Tree"
Method 2: Bottom-up recursion - O(n) runtime, O(logn) stack space
    traversing the entire list once
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # O(n) runtime, O(logn) stack space – Bottom-up recursion
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        current, length = head, 0
        while current is not None:
            current = current.next
            length += 1
        self.head = head
        return self.sortedListToBSTRecu(0, length)

    def sortedListToBSTRecu(self, start, end):
        if start == end:
            return None

        mid = start + (end - start) // 2
        left = self.sortedListToBSTRecu(start, mid)
        current = TreeNode(self.head.val)
        current.left = left
        self.head = self.head.next
        current.right = self.sortedListToBSTRecu(mid+1, end)
        return current

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    result = Solution().sortedListToBST(head)
    print result.val, result.left.val, result.right.val
