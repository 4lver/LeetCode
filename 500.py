#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
500. Keyboard Row
'''


class Solution(object):
	def findWords(self, words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		alphabet = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]
		result = []
		for i in words:
			k=0
			for n in range(len(alphabet)):
				if i[0].lower() in alphabet[n]:
					k = n
					break
			for j in i[1:]:
				if j.lower() not in alphabet[k]:
					#不能使用remove方法 因为指针下移会导致漏检查数据 
					break
			else:
				result.append(i)#这里else出现用来判断是否执行了break  如果执行了break 就不执行else后面的内容 如果没有执行break 那么就执行else后面的内容
		return words
		


if __name__ == '__main__':
	print Solution().findWords(["abdfs","cccd","a","qwwewm"])