# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree, return the inorder traversal of its nodes' values.
    For example:
        Given binary tree {1,#,2,3},
           1
            \
             2
            /
           3
        return [1,3,2].
Note: Recursive solution is trivial, could you do it iteratively?

Tags: Tree, Hash Table, Stack
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:    # not have left
                current = stack.pop()
                result.append(current.val)
                current = current.right
        return result

    def inorderTraversalMorris(self, root):
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
                    node.right = cur
                    cur = cur.left
                else:
                    result.append(cur.val)
                    node.right = None
                    prev = cur
                    cur = cur.right
        return result

    def inorderTraversalRecursive(self,root):
        if root:
            self.inorderTraversalRecursive(root.left)
            print root.val
            self.inorderTraversalRecursive(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print Solution().inorderTraversal(root)
    print Solution().inorderTraversalMorris(root)
    print Solution().inorderTraversalRecursive(root)
