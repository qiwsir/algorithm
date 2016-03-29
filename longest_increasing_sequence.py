#!/usr/bin/python
#coding: utf-8

def isBiggerCompare(a, b):
	return a > b

def findLIS(sequence, compare = isBiggerCompare):
	n = len(sequence)
	dp = [0 for i in range(n)]
	track = [-1 for i in range(n)]
	ans = 1
	for i in range(1, n):
		MAX = 0
		for j in range(i):
			if compare(sequence[i], sequence[j]) and MAX < dp[j]:
				MAX = dp[j]
				track[i] = j
				# track[i] sequence[i]作为最长上升序列末项的前一项
		dp[i] = MAX + 1
		# dp[i] 以sequence[i]结尾的最长上升序列长度
		if dp[i] > dp[ans]:
			ans = i
	ansList = [sequence[ans]]
	while track[ans] != -1:
		ans = track[ans]
		ansList.insert(0, sequence[ans])
	return ansList

if __name__ == '__main__':
	s = [3, 1, 2, 1, 4, 3, 5]
	print findLIS(s)
