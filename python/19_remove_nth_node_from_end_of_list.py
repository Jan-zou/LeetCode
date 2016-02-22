# !/usr/bin/env python
# coding: utf-8

'''
Description:
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.

Tags: Linked List, Two Pointers

设计两个指针p,q, q先走n步, p和q一起走, 直到q到尾节点, 删除p.next节点
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        for i in xrange(n):
            fast = fast.next

        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next


'''
with C

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode dummy = {-1, head};
    struct ListNode *p = &dummy;
    struct ListNode *q = &dummy;
    for(int i = 0; i < n; i++){
        q = q->next;
    }
    while(q->next){
        p = p->next;
        q = q->next;
    }
    struct ListNode *tpm = p->next;
    p->next = p->next->next;
    return dummy.next;
}
'''

