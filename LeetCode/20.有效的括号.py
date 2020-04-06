#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        box = {'(': ')', '[': ']', '{': '}'}
        boxes = []
        for i in s:
            if i in box:
                boxes.append(i)
            else:
                if boxes == 0:
                    return True
                elif box.values(i) == (boxes.pop()):
                    pass
                

        
# @lc code=end
