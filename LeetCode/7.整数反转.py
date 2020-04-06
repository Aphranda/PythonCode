#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        m = abs(x)
        n = len(str(m))
        lx = 0
        for i in range(n):
            if m > 10**i-1:
                num = (m%10**(i+1))*(10**(n-i-1))
                m = m -m%10**(i+1)
                lx +=(num//10**(n-1))*10**(n-i-1)
        if lx > 2147483648:
            return 0 
        elif x >= 0 and lx <= 2147483648:
            return lx
        elif x < 0 and lx <= 2147483648:
            return -lx


        
# @lc code=end

