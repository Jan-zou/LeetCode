# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Implement pow(x, n).   二分法求幂 x^n = x^(n//2) * x^(n//2) * x^(n%2)

Tags: Math, Binary Search
O(logn) runtime; O(1) space
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1.0/self.powRecu(x, -n)
        else:
            return self.powRecu(x,n)

    def powRecu(self, x, n):
        if n == 0:
            return 1.0

        if n % 2 == 0:    # 幂为偶数
            return self.powRecu(x*x, n//2)
        else:             # 幂为奇数
            return x * self.powRecu(x*x, n//2)


if __name__ == '__main__':
    print Solution().myPow(3, 5)
    print Solution().myPow(3, -5)
