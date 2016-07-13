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
Time: O(n), Space: O(1)

Roman literals from left to right("MXCVI")
Roman literals  Accumulated total
M               1000
MX              1000 + 10 = 1010
MXC             1010 + (100 – 2 * 10) = 1010 + 80 = 1090
MXCV            1090 + 5 = 1095
MXCVI           1095 + 1 = 1096
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

    def romanToInt2(self, s):
        prev, decimal = 0, 0
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}

        for i in xrange(len(s)):
            cur = numeral_map[s[i]]
            if cur > prev:
                decimal += cur - 2 * prev
            else:
                decimal += cur
            prev = cur
        return decimal


if __name__ == "__main__":
    print Solution().romanToInt("IIVX")
    print Solution().romanToInt("MMMCMXCIX")
    print Solution().romanToInt2("IIVX")
    print Solution().romanToInt2("MMMCMXCIX")
