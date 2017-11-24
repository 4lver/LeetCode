#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
728.Self Dividing Numbers
'''


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result=[]
        for i in xrange(left,right+1):
        	print i
        	if self.isDividingNumbers(i):
        		result.append(i)
        return result

    @staticmethod
    def isDividingNumbers(num):
    	L=list(str(num))
    	for i in L:
    		if int(i)==0:
    			return False
    		if num%int(i)!=0:
    			return False
    	return True

if __name__=="__main__":
	print Solution().selfDividingNumbers(1,22)
