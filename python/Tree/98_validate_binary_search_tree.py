# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree, determine if it is a valid binary search tree (BST).
    Assume a BST is defined as follows:
        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.
    Example 1:
        2
       / \
      1   3
    Binary tree [2,1,3], return true.
    Example 2:
        1
       / \
      2   3
    Binary tree [1,2,3], return false.

Tags: Tree, Depth-first Search
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # O(n^2) runtime, O(n) stack space - Brute force
    def isValidBST(self, root):
        if root is None:
            return True
        return self.isSubtreeLessThan(root.left, root.val) and self.isSubtreeGreaterThan(root.right, root.val) \
                and self.isValidBST(root.left) and self.isValidBST(root.right)

    def isSubtreeLessThan(self, node, val):
        if node is None:
            return True
        return node.val < val and self.isSubtreeLessThan(node.left, val) and self.isSubtreeLessThan(node.right, val)

    def isSubtreeGreaterThan(self, node, val):
        if node is None:
            return True
        return node.val > val and self.isSubtreeGreaterThan(node.left, val) and self.isSubtreeGreaterThan(node.right, val)


    # O(n) runtime, O(n) stack space - Top-down recursion
    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, float("-inf"), float("inf"))

    def valid(self, root, low, high):
        if root is None:
            return True

        # or if set low, hight is null; then check (low == null || root.val > low)
        return root.val > low and root.val < high \
               and self.valid(root.left, low, root.val) \
               and self.valid(root.right, root.val, high)


    # O(n) runtime, O(1) space - Morris Traversal Solution(inorder traversal)
    def isValidBST3(self, root):
        prev, cur = None, root
        while cur:
            if cur.left is None:
                if prev and prev.val >= cur.val:
                    return False
                prev = cur
                cur = cur.right
            else:    # 建线索（后继）
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    if prev and prev.val >= cur.val:
                        return False
                    node.right = None
                    prev = cur
                    cur = cur.right
        return True

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print Solution().isValidBST(root)
    print Solution().isValidBST2(root)
    print Solution().isValidBST3(root)
