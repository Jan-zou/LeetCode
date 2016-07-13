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
    # O(n) runtime, O(n) space - Stack
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

    # O(n) runtime, O(1) space - Morris
    def preorderTraversalMorris(self, root):
        result = []
        prev, cur = None, root
        while cur:
            if cur.left is None:
                result.append(cur.val)
                prev = cur    # cur刚刚被访问过
                cur = cur.right
            else:
                # 查找前驱
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:    # 还没线索化，则建立线索
                    result.append(cur.val) 􏴳􏲅􏲂􏰧􏰮􏴴􏴵􏴠􏱰􏳰􏱶􏰜# 仅此行的位置与中序不同
                    node.right = cur
                    prev = cur            # cur刚刚被访问过
                    cur = cur.left
                else:                     # 已经线索化，则删除线索
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
