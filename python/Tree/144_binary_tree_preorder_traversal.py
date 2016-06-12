# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree, return the preorder traversal of its nodes' values.
    For example:
        Given binary tree {1,#,2,3},
           1
            \
             2
            /
           3
        return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively?

Tags: Tree, Stack
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root

        while stack or current:
            if current:
                result.append(current.val)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return result

    def preorderTraversalMorris(self, root):
        result = []
        prev, cur = None, root
        while cur:
            if cur.left is None:
                result.append(cur.val)
                prev = cur
                cur = cur.right
            else:    # 建线索（后继）
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    result.append(cur.val)
                    node.right = cur
                    prev = cur
                    cur = cur.left
                else:
                    node.right = None
                    cur = cur.right
        return result

    def preorderTraversalRecursive(self, root):
        if root:
            print root.val
            self.preorderTraversalRecursive(root.left)
            self.preorderTraversalRecursive(root.right)

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print Solution().preorderTraversal(root)
    print Solution().preorderTraversalMorris(root)
    print Solution().preorderTraversalRecursive(root)
