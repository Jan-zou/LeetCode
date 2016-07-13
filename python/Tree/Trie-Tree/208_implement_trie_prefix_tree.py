# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Implement a trie with insert, search, and startsWith methods.
Note:
    You may assume that all inputs are consist of lowercase letters a-z.


Tags: Design, Trie
'''


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_string = False
        self.leaves = {}


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for c in word:
            if c not in current.leaves:
                current.leaves[c] = TrieNode()
            current = current.leaves[c]
        current.is_string = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.childSearch(word)
        if node:
            return node.is_string
        return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.childSearch(prefix) is not None


    def childSearch(self, word):
        current = self.root
        for c in word:
            if c in current.leaves:
                current = current.leaves[c]
            else:
                return None
        return current


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
