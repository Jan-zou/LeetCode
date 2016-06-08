# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
    For example:
        Given the below binary tree and sum = 22,
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1
        return
            [
               [5,4,11,2],
               [5,8,4,5]
            ]

Tags: Tree, Depth-first Search
Time: O(n); Space: O(h), h is height of binary tree
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result, current = [], []
        return self.pathSumRecu(result, current, root, sum)

    def pathSumRecu(self, result, current, root, sum):
        if root is None:
            return result

        if root.left is None and root.right is None and root.val == sum:
            result.append(current + [root.val])
            return result

        current.append(root.val)
        self.pathSumRecu(result, current, root.left, sum - root.val)
        self.pathSumRecu(result, current, root.right, sum - root.val)
        current.pop()
        return result


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.right = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    print Solution().pathSum(root, 22)
