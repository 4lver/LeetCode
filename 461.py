#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
461. Hamming Distance
'''

class Solution(object):
    def hammingDistance(self, x, y):
    	"""
        :type x: int
        :type y: int
        :rtype: int
        """
        newX = bin(x)[2:]
        newY = bin(y)[2:]
        rtype = 0
        count = 0
        print newX,newY
        if len(newX) >= len(newY):
        	newY = (len(newX)-len(newY)) * '0' + newY  
        else:
        	newX = (len(newY)-len(newX)) * '0' + newX
        print newX,newY
        for i in newX:
        	if i != newY[count]:
        		rtype += 1
        	count += 1
        return rtype

    def hammingDistance2(self, x, y):
    	"""
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')

print Solution().hammingDistance(3,5)
