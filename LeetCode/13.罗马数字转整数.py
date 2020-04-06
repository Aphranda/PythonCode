#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        example = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)-1):
            if (example[s[i]] >= example[s[i+1]]) and (i < len(s)-1):
                res += example[s[i]]
            elif (example[s[i]] < example[s[i+1]]) and (i < len(s)-1):
                res -= example[s[i]]
        return res + example[s[len(s)-1]]


             
# @lc code=end

