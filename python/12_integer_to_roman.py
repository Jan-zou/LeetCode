# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given an integer, convert it to a roman numeral.
    Input is guaranteed to be within the range from 1 to 3999.

    1~9: {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    10~90: {"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    100~900: {"C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
    1000~3000: {"M", "MM", "MMM"}.

Tags: Math, String
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        Roman = [
            ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["M", "MM", "MMM"]
        ]
        bit, RomanStr = 0, ''

        while num:
            temp = num % 10
            if temp != 0:
                RomanStr = Roman[bit][temp-1] + RomanStr
            num /= 10
            bit += 1

        return RomanStr

    def aintToRoman(self, num):
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        keyset, result = sorted(numeral_map.keys()), ""

        while num > 0:
            for key in reversed(keyset):
                while num / key > 0:
                    num -= key
                    result += numeral_map[key]
        return result

if __name__ == '__main__':
    print "Roman 1 is %s" % Solution().intToRoman(1)
    print "Roman 5 is %s" % Solution().intToRoman(5)
    print "Roman 37 is %s" % Solution().intToRoman(37)
    print "Roman 100 is %s" % Solution().intToRoman(100)
    print "Roman 2008 is %s" % Solution().intToRoman(2008)



