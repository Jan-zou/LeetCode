# !/usr/bin/env python
# coding: utf-8

'''
Description:
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    Example 1:
        nums1 = [1, 3]
        nums2 = [2]
        The median is 2.0
    Example 2:
        nums1 = [1, 2]
        nums2 = [3, 4]
        The median is (2 + 3)/2 = 2.5

Tags: Binary Search,  Array, Divide and Conquer

分析:
    （1）直观的解法:
            直接merge两个数组，然后求第k大的元素。时间为O(m+n)。
            不过仅需要第k大的元素，不需要整个排序；可以用一个计数器记录当前已经找到第m大的元素。
        同时使用两个指针pA和pB，分别指向A和B数组的第一个元素；使用类似merge sort的原理，
        如果数组A当前元素小，那么pA++同时m++，如果数组B当前元素小，那么pB++同时m++。
        最终当m=k时，就得到了想要的答案。O(k)的时间, O(1)的空间。但当k很接近m+n时，这个方法还是O(m+n)的。
    （2）O(log(m+n)) 的解法:
        将这道题转化为更通用的形式是: 给定两个已经排序好的数组，找到两者所有元素中第k小的元素。
        median = (m+n)//2  是第(median+1)小的数
        假设数组A和B的元素个数都大于k/2，将A的第k/2个元素(即A[k/2 -1])和B的第k/2个元素(即B[k/2 -1])比较:
             + A[k/2 -1] < B[k/2 -1]: 意味着A[0]到A[k/2 -1]都在topk元素范围内
             + A[k/2 -1] > B[k/2 -1]: 意味着B[0]到B[k/2 -1]都在topk元素范围内
             + A[k/2 -1] == B[k/2 -1]: 找到第k大的元素，直接返回A[k/2 -1]或B[k/2 -1]
        递归函数的终止条件:
             + 当A或B为空时，直接返回B[k-1]或A[k-1]
             + 当k=1时，返回min(A[0], B[0])
             + 当A[k/2 -1] == B[k/2 -1]时，返回A[k/2 -1]或B[k/2 -1]
'''

class Solution(object):
    # O(m+n) runtime; O(1) space
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result, i, j = [], 0, 0
        m, n = len(nums1), len(nums2)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                result.append(nums2[j])
                j += 1
            else:
                result.extend([nums1[i], nums2[j]])
                i += 1
                j += 1

        while i < m:
            result.append(nums1[i])
            i += 1

        while j < n:
            result.append(nums2[j])
            j += 1

        if (m+n) % 2 == 1:
            return result[(m+n)//2]
        else:
            return (result[((m+n)//2)-1] + result[(m+n)//2]) / 2.0

    # O(k) runtime; O(1) space
    def findMedianSortedArrays2(self, nums1, nums2):
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return self.findK(nums1, nums2, total/2)
        else:
            return (self.findK(nums1, nums2, total/2 - 1) + self.findK(nums1, nums2, total/2)) / 2.0

    def findK(self, nums1, nums2, k):  # k: index
        m, n = len(nums1), len(nums2)
        i, j, index, kth = 0, 0, -1, 0

        while index < k and i < m and j < n:
            if nums1[i] <= nums2[j]:
                kth = nums1[i]
                i += 1
                index += 1
            else:
                kth = nums2[j]
                j += 1
                index += 1

        while index < k and i < m:
            kth = nums1[i+k-index-1]
            i += 1
            index += 1

        while index < k and j < n:
            kth = nums2[j+k-index-1]
            j += 1
            index += 1

        return kth

    # O(log(m+n)) runtime; O(log(m+n)) space
    def findMedianSortedArrays3(self, nums1, nums2):
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return self.find_kth(nums1, nums2, total/2 + 1)
        else:
            return (self.find_kth(nums1, nums2, total/2) + self.find_kth(nums1, nums2, total/2 + 1)) / 2.0

    # find kth number, index k+1
    def find_kth(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        # always assume that m is equal or smaller than n
        if m > n:
            return self.find_kth(nums2, nums1, k)

        if m == 0:
            return nums2[k-1]
        if n == 0:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])

        # divide k into two parts
        pa = min(m, k/2)
        pb = k - pa
        if nums1[pa-1] < nums2[pb-1]:
            return self.find_kth(nums1[pa:], nums2, k - pa)
        elif nums1[pa-1] > nums2[pb-1]:
            return self.find_kth(nums1, nums2[pb:], k - pb)
        else:
            return nums1[pa-1]


if __name__ == '__main__':
    print Solution().findMedianSortedArrays([1,3], [2])    # output: 2
    print Solution().findMedianSortedArrays2([1,2], [3,4])    # output: 2.5
    print Solution().findMedianSortedArrays3([1,3], [2])    # output: 2
    print Solution().findMedianSortedArrays3([1,2], [3,4])    # output: 2.5
