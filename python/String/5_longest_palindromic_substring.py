# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given a string S, find the longest palindromic substring in S.
    You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Tags: String
Time: O()
Space: O()

最长回文子串
1. 暴力枚举: 求出每一个子串判断是不是回文，找到最长的那个。O(n^3) 找到所有子串O(n^2),检查是否为回文O(n)
2. 中心扩展法     Time: O(n^2); Space: O(1)
3. 动态规划       Time: O(n^2); Space: O(n^2)
4. Manacher算法  Time: O(n); Space: O(n)
'''

class Solution(object):
    '''
    动态规划的方法通过一些记录来避免暴力解法中的很多重复的判断。如'ababa'，已经知道'bab'是回文时很明显'ababa'也是回文。
    设状态为P(i,j), 表示字符串s[i,j]是否为回文串, 状态转移方程为:
        i=j,   P(i,j)= true
        j=i+1, P(i,j)= (s[i]==s[j])
        j>i+1, P(i,j)= (s[i]==s[j]) and P(i+1, j-1)
    '''
    def longestPalindrome(self, s):
        import numpy
        if len(s) <= 1:
            return s

        start, max_len = 0, 0
        n = len(s)
        dp = numpy.zeros((n, n))

        for i in xrange(n):    # 长度为1，全是回文
            dp[i][i] = 1
        for i in xrange(n-1):  # 长度为2，相等是回文
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                max_len = 2
                start = i
        for k in xrange(3, n):
            for i in xrange(n-k):
                j = i + k - 1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    start = i
                    max_len = k
        return s[start:max_len+1]


    '''
    如果一段字符串是回文，那么以某个字符为中心的前缀和后缀都是相同的。
    因此枚举中心位置，然后再在该位置上用扩展法，记录并更新得到的最长的回文长度。(回文串分奇偶数长度两种情况)
    对给定的字符串S，分别以该字符串S中的每一个字符c为中心向两边扩展，记录下以字符c为中心的回文子串的长度。
    '''
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        result = ''
        for i in xrange(len(s)-1):
            p1 = self.expand(s, i, i)   # 奇数
            if len(p1) > len(result):
                result = p1
            p2 = self.expand(s, i, i+1)    # 偶数
            if len(p2) > len(result):
                result = p2
            i += 1
        return result

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]


    '''
    Manacher算法
    http://articles.leetcode.com/longest-palindromic-substring-part-ii
    使用center, right两个参数配合在每次循环中直接对P[i]快速赋值,
    在计算以i为中心的回文子串中，不必每次都从1开始比较，减少了比较次数。
    时间复杂度分析:
        尽管代码里面有两层循环，通过amortized analysis我们可以得出，Manacher的时间复杂度是线性的。
        由于内层的循环只对尚未匹配的部分进行，因此对于每一个字符而言，只会进行一次，因此时间复杂度是O(n)。
    '''
    def longestPalindrome3(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = self.preProcess(s)
        # P[]记录以每个字符为中心的最长回文半径(P[i]-1 是以i为中心的回文子串在原串中的长度)
        # 遍历P[]找到最大的P[i]就可以求出最长回文子串的长度及位置
        palindrome = [0] * len(T)
        center, right = 0, 0    # 中心center, 边界right=center+P[center]
        for i in xrange(1, len(T) - 1):
            i_mirror = 2 * center - i    # i关于center的对称点
            # i小于边界时，以i_mirror为中心的回文子串包含在以center为中心的回文子串；
            # 根据回文对称的特性，以i为中心的回文子串也应包含在以center为中心的回文子串；
            # 根据边界，取较小的
            if right > i:
                palindrome[i] = min(right - i, palindrome[i_mirror])
            else:
                palindrome[i] = 0

            # Attempt to expand palindrome centered at i
            while T[i + 1 + palindrome[i]] == T[i - 1 - palindrome[i]]:
                palindrome[i] += 1

            # if palindrome centered at i expand past right,(越界)
            # adjust center based on expanded palindrome
            if i + palindrome[i] > right:
                center, right = i, i + palindrome[i]

        max_len, max_center = 0, 0
        for i in xrange(1, len(T) - 1):  # '^'
            if palindrome[i] > max_len:
                max_len = palindrome[i]
                max_center = i
        start = (max_center - max_len - 1) / 2    # 最长回文子串在原串中的起始位置
        return s[start : start + max_len]

    def preProcess(self, s):
        # 在各个字符串中间插入一个特殊字符（将所有可能的奇/偶数长度的回文子串都转换成奇数长度）
        if not s:
            return '^$'
        string = '^'
        for i in s:
            string += '#' + i
        string += '#$'
        return string


if __name__ == '__main__':
    print Solution().longestPalindrome('babcbabcbaccba')
    print Solution().longestPalindrome2('babcbabcbaccba')
    print Solution().longestPalindrome3('babcbabcbaccba')
