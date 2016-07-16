# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
	Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
	For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Tags: Bit Manipulation
'''

class Solution(object):
	# The key idea: for any number n, doing a bit-wise AND of n and n - 1 flips the least-significant 1-bit in n to 0.
	# O(1) runtime; O(1) space
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            n = n & (n-1)
            result += 1
        return result

    def hammingWeight2(self, n):
    	result = 0
    	while n:
    		if n % 2 == 1:
    			result += 1
    		n /= 2
    	return result
