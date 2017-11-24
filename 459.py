#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
459. Repeated Substring Pattern
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s+s)[1:-1].find(s)!=-1


if __name__=='__main__':
	print Solution().repeatedSubstringPattern("ababc")