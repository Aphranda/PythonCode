#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0
        box = [s[0]]
        vol = []
        n = len(s)-1
        for i in range(n):
            while s[i+1] in box:
                box.pop(0)
            box.append(s[i+1])
            length = len(box)
            vol.append(length)
        return max(vol)

# @lc code=end
"""
1.滑动窗口
    -窗口首先不断向后延展，扩大窗口
        定义窗口 box -> list 窗口扩大 box.append()
    -当遇到相同字符时，窗口从头部开始缩小
        定义循环while  删除字符 box.pop(index) index 
    -当重复项被删除时，继续往后延展，扩大窗口
        循环结束break box.append()
    -记录每一次循环时的窗口大小，从中找出最大值
        窗口大小 vol = []
"""
