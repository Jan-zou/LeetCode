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
    # O(n) runtime, O(n) space - Stack
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

    # O(n) runtime, O(1) space - Morris
    def postorderTraversalMorris(self, root):
        dummy = TreeNode(0)
        dummy.left = root

        result, cur, prev = [], dummy, None
        while cur:
            if cur.left is None:
                prev = cur
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:    # 还没线索化，则建立线索
                    node.right = cur
                    prev = cur
                    cur = cur.left
                else:                     # 已经线索化，则访问节点，并删除线索
                    result += self.traceBack(cur.left, node)
                    # result += self.reversePrint(cur.left, node)
                    node.right = None
                    prev = cur
                    cur = cur.right
        return result

    def traceBack(self, fromNode, toNode):
        result, cur = [], fromNode
        while cur is not toNode:
            result.append(cur.val)
            cur = cur.right
        result.append(toNode.val)
        result.reverse()
        return result

    def reverse(self, fromNode, toNode):
        if fromNode == toNode:
            return;

        x, y, z = fromNode, fromNode.right, TreeNode(0)
        while x != toNode:
            z = y.right
            y.right = x
            x = y
            y = z

    def reversePrint(self, fromNode, toNode):
        result = []
        self.reverse(fromNode, toNode)

        p = toNode
        while True:
            result.append(p.val)
            if p == fromNode:
                break
            p = p.right

        self.reverse(toNode, fromNode)
        return result


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
