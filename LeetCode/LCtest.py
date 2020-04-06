
print(ord("("), ord(")"))
print(ord("["), ord("]"))
print(ord("{"), ord("}"))

class Solution:
    def isValid(self, s: str) -> bool:
        box = []
        stack = []
        for i in s:
            box.append(ord(i))
        print(box)
        for i in box:
            if i == 40 or i == 91:
                stack.append(i)
        print(stack)


s = r"()[]{}"
lc = Solution()
lc.isValid(s)

"""
1.符号转化成ASCII码
ord()
2.遍历ASCII码，选出每个符号的位置
3.栈-
左括号出栈，右括号出栈
逐步让最内括号对出栈
4.
"""