#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
657. Judge Route Circle
'''

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = [0,0]
        for i in moves:
        	if i == 'U':
        		pos[0]+=1
        	if i == 'D':
        		pos[0]-=1
        	if i == 'L':
        		pos[1]-=1
        	if i == 'R':
        		pos[1]+=1
        if pos == [0,0]:
        	return True
        else:
        	return False



print Solution().judgeCircle("UU")     		