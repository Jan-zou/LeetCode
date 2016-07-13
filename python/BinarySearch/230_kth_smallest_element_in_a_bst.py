# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note:
    You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
Follow up:
    What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
    How would you optimize the kthSmallest routine?
Hint:
    1. Try to utilize the property of a BST.
    2. What if you could modify the BST node's structure?
    3. The optimal runtime complexity is O(height of BST).

Tags: Tree, Binary Search
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 中序遍历得到递增序列; Time: O(n); Space: O(n)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        tree = self.inorder(root)
        return tree[k-1]

    def inorder(self,root):
        stack, result = [], []
        current = root

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.val)
                current = current.right

        return result

    # Time: O(max(h,k)); Space: O(n)
    def kthSmallest2(self, root, k):
        rank, current, stack = 0, root, []
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                rank += 1
                if rank == k:
                    return current.val
                current = current.right
