# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given an array and a value, remove all instances of that value in place and return the new length.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Tags: Array, Two Pointers
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        result = len(nums) - 1
        i = 0
        while i <= result:
            if nums[i] == val:
                nums[i], nums[result] = nums[result], nums[i]
                result -= 1
            else:
                i += 1

        return result + 1


if __name__ == '__main__':
    Solution().removeElement([1, 2, 3, 4, 5, 2, 2], 2)


'''
# with C

int removeElement(int* nums, int numsSize, int val) {
    int index = 0;
    for(int i=0; i<numsSize; i++){
        if(nums[i] != val){
            nums[index] = nums[i];
            index++;
        }
    }
    return index;
}
'''
