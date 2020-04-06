#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs:List[str]) -> str:
        res = ""
        for word in zip(*strs):
            if len(set(word)) == 1:
                res += word[0]
            else:
                break
        return res
        
# @lc code=end

