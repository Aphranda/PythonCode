class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        right = []
        left = []
        string = s
        even = []
        odd = []
        index = {}
        if n < 2:
            return n
        for i in range(n-1):
            if s[i] == s[i+1]:
                right.append(i)
        if len(right) >= 1:
            for i in right:
                r = i
                l = i + 1
                while r >= 0 and l <= len(string)-1 and string[r] == string[l]:
                    r -= 1
                    l += 1
                    # print(i, r, l, string[r+1:l])
                even.append(string[r+1:l])
        for i in range(n-2):
            if s[i] == s[i+2]:
                left.append(i+1)
        if len(left) >= 1:
            for i in left:
                r = i
                l = i 
                while r >= 0 and l <= len(string)-1 and string[r] == string[l]:
                    r -= 1
                    l += 1
                    # print(i, r, l, string[r+1:l])
                odd.append(string[r+1:l])
        # print(right, left)
        element = even + odd
        for i,n  in enumerate(element):
            index[i] = len(n)
        ret = max(index, key = lambda x: index[x])
        print(element[ret])
        return element
            
s = 'cbbd'
test = Solution()
test.longestPalindrome(s)

"""
目标：寻找最长回文子串
关键词：最长 回文 字串
方法：尝试扩散法
    一、每向前进一位就尝试判断回文
    进位：for循环 if 偶数回文，elif奇数回文
    二、回文停止时输出回文数
    输出记号标识位signal，转化回文数输出
    三、特殊情况

"""

            








