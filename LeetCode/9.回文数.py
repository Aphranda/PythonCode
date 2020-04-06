#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x != 0):
            return False
        res = 0
        while x > res:
            res = res*10 + x%10
            x = x//10
            print(res, x)
        return x == res or res//10 == x
        
# @lc code=end

