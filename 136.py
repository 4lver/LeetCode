#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
136. Single Number
'''

import operator

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor,nums)