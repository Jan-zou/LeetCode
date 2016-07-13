# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Two elements of a binary search tree (BST) are swapped by mistake.
    Recover the tree without changing its structure.
Note:
    A solution using O(n) space is pretty straight forward.
    Could you devise a constant space solution?

Tags: Tree, Depth-first Search

使用常数空间O(1): Mirror中序遍历 (线索二叉树)
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()
            return repr(serial)
        else:
            return None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        broken = [None, None]
        prev, cur = None, root
        while cur:
            if cur.left is None:
                self.detect(broken, prev, cur)
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
                    self.detect(broken, prev, cur)
                    prev = cur
                    cur = cur.right

        broken[0].val, broken[1].val = broken[1].val, broken[0].val
        return root


    def detect(self, broken, prev, cur):
        if prev and prev.val > cur.val:
            if broken[0] is None:
                broken[0] = prev
            broken[1] = cur


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    print root
    print Solution().recoverTree(root)
