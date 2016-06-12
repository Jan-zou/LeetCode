# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree, return the postorder traversal of its nodes' values.
    For example:
        Given binary tree {1,#,2,3},
           1
            \
             2
            /
           3
        return [3,2,1].
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        current, last = root, None

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                parent = stack[-1]
                if parent.right in (None, last):
                    result.append(parent.val)
                    last = stack.pop()
                else:
                    current = parent.right
        return result

    def postorderTraversalMorris(self, root):
        dump = TreeNode(0)
        dump.left = root

        prev, cur = None, dump
        while cur:
            if cur.left is None:
                prev = cur
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    self.reversePrint(cur.left, node)
                    node.right = None
                    prev = cur
                    cur = cur.right

    def reverse(self, fromNode, toNode):
        if fromNode == toNode:
            return;

        x, y, z = fromNode, fromNode.right, TreeNode(0)
        while True:
            z = y.right
            y.right = x
            x = y
            y = z
            if x == toNode:
                break

    def reversePrint(self, fromNode, toNode):
        self.reverse(fromNode, toNode)

        p = toNode
        while True:
            print p.val
            if p == fromNode:
                break
            p = p.right

        self.reverse(toNode, fromNode)


    def postorderTraversalRecursive(self, root):
        if root:
            self.postorderTraversalRecursive(root.left)
            self.postorderTraversalRecursive(root.right)
            print root.val

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print Solution().postorderTraversal(root)
    print Solution().postorderTraversalMorris(root)
    print Solution().postorderTraversalRecursive(root)
