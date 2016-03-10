# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.

    1~9: {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    10~90: {"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    100~900: {"C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
    1000~3000: {"M", "MM", "MMM"}.

Tags: Math, String

从前往后扫描，用一个临时变量记录分段数字。
如果当前比前一个大，说明这段的值是当前这个值减去上一个值；否则，将当前值加入到结果中，然后开始下一段记录。
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        decimal = 0
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}

        for i in xrange(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i-1]]:
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i-1]]
            else:
                decimal += numeral_map[s[i]]
        return decimal

if __name__ == "__main__":
    print Solution().romanToInt("IIVX")
    print Solution().romanToInt("MMMCMXCIX")
