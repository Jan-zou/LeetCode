# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Merge k sorted linked lists and return it as one sorted list.
    Analyze and describe its complexity.

Tags: Divide and Conquer, Linked List, Heap

Solution 1: Brute force
    k个长度为n的list依次合并; 时间复杂度为2n+3n+...+kn=O(nk^2), 空间复杂度为O(1)
Solution 2: Heap
    利用最小堆结构heap, 每次pop最小值来merge列表; Time: O(nklogk), Space: O(k)
Solution 3: Divide and Conquer using two way merge
    merges two lists at a time, so the number of lists reduces from:
            k -> k/2 -> k/4 -> ... -> 2 -> 1
    the size of the lists increases from:
             n -> 2n -> 4n -> .. -> 2^(logk)n
    (Note that the lists could subdivide itself at most log(k) times)
    Time: O(nklogk), Space: O(1)
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
    # solution 2: heap
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
                heapq.heappush(heap, (smallest.next.val, smallest.next))  # log(k)

        return dummy.next


    # solution 3: Divide and Conquer
    def mergeKLists2(self, lists):
        if not lists:
            return None

        end = len(lists) - 1
        while end > 0:
            start = 0
            while start < end:
                lists.insert(start, self.merge2Lists(lists[start], lists[end]))
                del lists[start]
                del lists[end]
                start += 1
                end -= 1
        return lists[0]

    def merge2Lists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy

        if l1 == l2:
            return l1

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return dummy.next


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(5)
    list2 = ListNode(2)
    list2.next = ListNode(6)
    list3 = ListNode(3)
    list3.next = ListNode(7)

    print Solution().mergeKLists([list1, list2, list3])
    print Solution().mergeKLists2([list1, list2, list3])
