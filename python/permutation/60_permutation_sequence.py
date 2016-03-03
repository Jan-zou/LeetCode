# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    The set [1,2,3,…,n] contains a total of n! unique permutations.
    By listing and labeling all of the permutations in order,
    We get the following sequence (ie, for n = 3):

        1. "123"
        2. "132"
        3. "213"
        4. "231"
        5. "312"
        6. "321"
    Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

Tags: Backtracking, Math

康拓编码:
1. 康拓展开:
    X=an*(n-1)!+an-1*(n-2)!+...+ai*(i-1)!+...+a2*1!+a1*0!
    其中，ai为当前未出现的元素中是排在第几个(从0开始)
2. 找到一种排列是全排序中的第几个？
3. 找到全排序中的第k个排序？
'''

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq = ""
        k = k - 1
        fact = math.factorial(n - 1)    # (n-1)!
        perm = [i for i in xrange(1, n + 1)]
        for i in reversed(xrange(n)):
            curr = perm[k / fact]
            seq += str(curr)
            perm.remove(curr)
            if i > 0:
                k %= fact
                fact /= i
        return seq


if __name__ == '__main__':
    Solution().getPermutation(3, 2)
