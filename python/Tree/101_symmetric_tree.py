# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
            1
           / \
          2   2
         / \ / \
        3  4 4  3
    But the following [1,2,2,null,3,null,3] is not:
            1
           / \
          2   2
           \   \
           3    3
Note:
    Bonus points if you could solve it both recursively and iteratively.

Tags: Tree, Depth-first Search, Breadth-first Search
Time: O(n); Space: O(h), h is height of binary tree
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Iterative solution
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        stack = [root.left, root.right]
        while stack:
            p, q = stack.pop(), stack.pop()

            if p is None and q is None:
                continue

            if p is None or q is None or p.val != q.val:
                return False

            stack.append(p.left)
            stack.append(q.right)

            stack.append(p.right)
            stack.append(q.left)
        return True


    # Recursively solution
    def isSymmetric2(self, root):
        if root is None:
            return True

        return self.isSymmetricRecu(root.left, root.right)

    def isSymmetricRecu(self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None or left.val != right.val:
            return False

        return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)


if __name__ == '__main__':
    root = TreeNode(1)
    print Solution().isSymmetric(root)
    print Solution().isSymmetric2(root)
