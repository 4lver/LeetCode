#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
485. Max Consecutive Ones
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        tem_num=0
        for i in xrange(len(nums)):
        	if nums[i] == 1 :
        		tem_num+=1
        	if nums[i] == 0:
        		tem_num=0
        	if tem_num > result:
        		result = tem_num
        return result


if __name__=='__main__':
	print Solution().findMaxConsecutiveOnes([1,1,1,1,0,1,1,0,1,1,1,1,1,0])