# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

    Example 1:
    Given words = ["bat", "tab", "cat"]
    Return [[0, 1], [1, 0]]
    The palindromes are ["battab", "tabbat"]
    Example 2:
    Given words = ["abcd", "dcba", "lls", "s", "sssll"]
    Return [[0, 1], [1, 0], [3, 2], [2, 4]]
    The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

Tags: Hash Table, String, Trie

利用字典wdict保存单词 -> 遍历单词列表words，记单词为word，下标为idx：{word:id}
利用set来保存有效的回文对下标
1.若当前单词word本身为回文，且words中存在空串，则将空串下标bidx与idx加入ans
2.若当前单词的逆序串在words中，则将逆序串下标ridx与idx加入ans
3.for循环将当前单词word拆分为左右两半left，right
    + 若left为回文，且right的逆序串在wdict中，则将right的逆序串下标rridx与idx加入ans
    + 若right为回文，且left的逆序串在wdict中，则将idx与left的逆序串下标rlidx加入ans
时间复杂度: O(k*n^2) (k为单词个数，n为单词长度)

或用Trie树来存储单词列表，每次插入时记录单词index值。
Trie树插入、查找的时间复杂度均为O(N)，其中N为字符串长度。
'''


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wdict = {word:idx for idx, word in enumerate(words)}
        ans = set()

        for idx, word in enumerate(words):
            if '' in wdict and word != '' and self.isPalindrome(word):
                bidx = wdict['']
                ans.add((idx, bidx))
                ans.add((bidx, idx))

            rword = word[::-1]
            if rword in wdict:
                ridx = wdict[rword]
                if idx != ridx:
                    ans.add((idx, ridx))
                    ans.add((ridx, idx))

            for x in xrange(1, len(word)):
                left, right = word[:x], word[x:]
                rleft, rright = left[::-1], right[::-1]
                if self.isPalindrome(left) and rright in wdict:
                    ans.add((wdict[rright], idx))
                if self.isPalindrome(right) and rleft in wdict:
                    ans.add((idx, wdict[rleft]))

        return list(ans)


    def isPalindrome(self, word):
        i, j = 0, len(word)-1
        while i < j:
            if word[i].lower() != word[j].lower():
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    print Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
