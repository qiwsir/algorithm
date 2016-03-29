# 问题简介
最长公共上升子序列，longest increasing sequence，简称LCIS
# 思路
这个问题要由动态规划来解决，时间复杂度是O(n<sup>2</sup>)，空间复杂度是O(n)，建立dp[n]和track[n]    
意义：
----
* dp[i]：以数据a[i]结尾的最长上升序列长度
* track[i]：数据a[i]作为最长上升序列末项的前一项索引


