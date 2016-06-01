# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Merge k sorted linked lists and return it as one sorted list.
    Analyze and describe its complexity.

Tags: Divide and Conquer, Linked List, Heap
Time: O(nlogk); Space: O(k)  利用最小堆结构，每次pop最小值来merge列表
'''
import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        heap = []

        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))

        while heap:
            smallest = heapq.heappop(heap)[1]  # pop first element(min)
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))

        return dummy.next


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list2 = ListNode(2)
    list2.next = ListNode(5)
    list3 = ListNode(3)
    list3.next = ListNode(6)

    print Solution().mergeKLists([list1, list2, list3])
