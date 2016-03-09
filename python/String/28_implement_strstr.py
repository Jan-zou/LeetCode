# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Implement strStr().
    Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Tags: Two Pointers, String

返回needle在haystack中第一次出现的位置，如果needle不在haystack中，则返回-1。(子串长度为m)
+ 暴力匹配  Time: O(n*m)  Space: O(1)
+ KMP      Time: O(n+m)  Space: O(m)
+ Boyer-Mooer
+ Rabin-Karp
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack) - len(needle) + 1
        i = 0
        while i < n:
            j, k = i, 0    # index: 字符串j ; 子串k
            while j < len(haystack) and k < len(needle) and haystack[j] == needle[k]:
                j += 1
                k += 1

            if k == len(needle):
                return i

            i += 1

        return -1


# KMP
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        if len(haystack) < len(needle):
            return -1

        i = self.KMP(haystack, needle)
        if i > -1:
            return i
        else:
            return -1

    # 不回溯，haystach中的i不动，移动needle中的j跳到k, k=next(j)表示子串中每个j不匹配时可能跳转的位置
    def KMP(self, text, pattern):
        next = self.getNext(pattern)
        j = -1
        for i in xrange(len(text)):
            while j > -1 and pattern[j + 1] != text[i]:
                j = next[j]
            if pattern[j + 1] == text[i]:
                j += 1
            if j == len(pattern) - 1:
                return i - j
        return -1

    def getNext(self, pattern):
        next = [-1] * len(pattern)    # 当前不匹配为首位时，next(j)=-1
        j = -1
        for i in xrange(1, len(pattern)):
            while j > -1 and pattern[j + 1] != pattern[i]:
                j = next[j]
            if pattern[j + 1] == pattern[i]:
                j += 1
            next[i] = j
        return next


if __name__ == '__main__':
    print Solution().strStr('a', '')
    print Solution().strStr('mississippi', 'a')
    print Solution().strStr('abababcdab', 'bcd')
    print Solution2().strStr('a', '')
    print Solution2().strStr('mississippi', 'a')
    import pdb
    pdb.set_trace()
    print Solution2().strStr('abababcdab', 'bcd')
