# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it is able to trap after raining.

    For example,
    Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Tags: Array, Stack, Two Pointers
'''

class Solution(object):
    # O(n) runtime; O(1) space
    # 找到中间最大值，左右两边分别找次大值向中间逼近
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result, top = 0, 0
        for i in xrange(len(height)):
            if height[top] < height[i]:
                top = i

        second_top = 0
        for i in xrange(top):
            if height[second_top] < height[i]:
                second_top = i
            result += height[second_top] - height[i]

        second_top = len(height) - 1
        for i in reversed(xrange(top, len(height))):
            if height[second_top] < height[i]:
                second_top = i
            result += height[second_top] - height[i]
        return result


    # O(n) runtime, O(1) space
    def trap2(self, height):
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while l < r and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water


    # O(n) runtime, O(n) space - 单调递减栈
    def trap3(self, height):
        result, stack = 0, []
        for i in xrange(len(height)):
            mid_height = 0
            while stack:
                [pos, h] = stack.pop()
                result += (min(h, height[i]) - mid_height) * (i - pos - 1)
                mid_height = h

                if height[i] < h:
                    stack.append([pos, h])
                    break
            stack.append([i, height[i]])
        return result


if __name__ == "__main__":
    print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print Solution().trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print Solution().trap3([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
