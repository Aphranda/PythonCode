class IntNode(object):
    def __init__(self, i, n):
        self.item = i
        self.next = n
        self.prev = p


class SList(object):
    def __init__(self, x = None):
        self.__head = IntNode(49, None, None)
        self.__head.next = self.__head
        self.__head.prev = self.__head
        if x is None:
            self.__size = 0
        else:
            # now_node = IntNode(x, self.__head, self.__head)
            # self.__head.next = now_node
            # self.__head.prev = now_node
            self.__head.next = IntNode(x, self.__head, self.__head)
            self.__head.prev = IntNode(x, self.__head, self.__head)
            self.__head.next = IntNode(x, None)
            self.__size = 1  # 缓存思想 (可以存最大值，最小值，总和, 最后一个元素)

    def size(self):
        return self.__size

    def add_first(self, x):
        original_first = self.__head.next
        new_first = IntNode(x, original_first, self.__head)
        original_first.prev = new_first
        self.__head.next = new_first
        self.__size += 1

    def add_last(self, x):
        self.__size += 1
        p = self.__head
        while p.next is not None:
            p = p.next
        p.next = IntNode(x, None)

    def get_first(self):
        return self.__head.next.item


class Stack:
    def __init__(self):
        self.__data = []

    def push(self, x):
        self.__data.append(x)

    def pop(self):
        return self.__data.pop()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())








# l = SList()
# l.add_last(1)
# print(l.get_first()) 
# l.add_first(15)
# l.add_first(20)
# l.add_first(5)
# print(l.get_first())
# l.add_last(20)
# print(l.size())
