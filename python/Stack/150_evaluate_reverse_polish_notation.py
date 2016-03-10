# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    Valid operators are +, -, *, /. Each operand may be an integer or another expression.
    Some examples:
      ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
      ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Tags: Stack
Time: O(n)
Space: O(n)
'''
# import operator

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import operator
        stack = []
        operator = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else:
                x, y = stack.pop(), stack.pop()
                stack.append(int(operator[token](float(y), x)))
        return stack.pop()


if __name__ == '__main__':
    print Solution().evalRPN(["2", "1", "+", "3", "*"])
    print Solution().evalRPN(["4", "13", "5", "/", "+"])

