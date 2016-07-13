# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
    If the fractional part is repeating, enclose the repeating part in parentheses.
    For example,
        Given numerator = 1, denominator = 2, return "0.5".
        Given numerator = 2, denominator = 1, return "2".
        Given numerator = 2, denominator = 3, return "0.(6)".
Hint:
    1. No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
    2. Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
    3. Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

Tags: Hash Table, Math
Time:  O(logn), where logn is the length of result strings
Space: O(1)
'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        dvd, dvs = abs(numerator), abs(denominator)
        integer, decimal, dict = '', '', {}

        if dvd > dvs:
            integer = str(dvd/dvs)
            dvd %= dvs
        else:
            integer = '0'

        if dvd > 0:
            integer += '.'

        idx = 0
        while dvd:
            if dvd in dict:
                decimal = decimal[:dict[dvd]] + '(' + decimal[dict[dvd]:] + ')'
                break

            dict[dvd] = idx
            idx += 1

            dvd *= 10
            decimal += str(dvd/dvs)
            dvd %= dvs

        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            return "-" + integer + decimal
        else:
            return integer + decimal

if __name__ == "__main__":
    print Solution().fractionToDecimal(1, 2)
    print Solution().fractionToDecimal(2, 1)
    print Solution().fractionToDecimal(2, 3)
