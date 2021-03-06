# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Implement atoi to convert a string to an integer.
    Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
    Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

    Update (2015-02-10):
    The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

    Requirements for atoi:
    The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
    Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
    The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
    If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Tags: Math, String

Time: O(n), Space: O(1)
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647    # 2^31 - 1
        INT_MIN = -2147483648
        result = 0

        if not str:
            return result

        i = 0
        # 空格
        while i < len(str) and str[i] == ' ':
            i += 1
        # 正负号
        sign = 1
        if str[i] == '-':
            sign = -1
            i += 1
        elif str[i] == '+':
            i += 1

        while i < len(str) and str[i] >= '0' and str[i] <= '9':
            if result > INT_MAX / 10 or (result == INT_MAX / 10 and ord(str[i])-ord('0') > INT_MAX % 10):
                # handle overflow
                if sign > 0:
                    return INT_MAX
                else:
                    return INT_MIN

            result = result * 10 + ord(str[i]) - ord('0')    # ord(str)->ASCII  chr(ASCII) ->str
            i += 1

        return sign * result


if __name__ == '__main__':

    print Solution().myAtoi("0")
    print Solution().myAtoi("1")
    print Solution().myAtoi("-123")
    print Solution().myAtoi("123")
    print Solution().myAtoi("2147483647")
    print Solution().myAtoi("-2147483648")
    # 不规则有效输入
    print Solution().myAtoi("+43")          # 43
    print Solution().myAtoi("-3924x8fc")    # -3924
    # 溢出
    print Solution().myAtoi("2147483648")     # 2147483647
    print Solution().myAtoi("-2147483649")    # -2147483648
    # 无效输入
    print Solution().myAtoi("")      # 0
    print Solution().myAtoi("++c")   # 0
    print Solution().myAtoi("++1")   # 0

