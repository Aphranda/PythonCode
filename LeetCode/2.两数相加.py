#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def change(ls):
            l = ls.val
            a = 1
            while ls.next != None:
                ls = ls.next
                l += ls.val*10**a
                a += 1
            return l
 
        def rebeck(ls):
            head = ListNode(ls[0])
            r = head
            p = head
            for i in ls[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
            return r
        
        c = change(l1) + change(l2)
        ls = []
        s = list(reversed(list(str(c))))
        for i in s:
            ls.append(int(i))
        return rebeck(ls)


# @lc code=end

