# -*- coding:utf-8 -*-
"""
作者：xiyang
日期：2022年06月12日
功能解释：单链表的功能实现
"""

class Node(object):
    """ 单链表节点 类"""
    def __init__(self, element):
        self.element = element
        self.next = None

class SingleLinkList(object):
    """ 单链表 """
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """判断是否为空"""
        return self._head == None

    def length(self):
        """长度"""
        cur = self._head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历单链表"""
        cur = self._head
        while cur != None:
            print(cur.element, end=" ")
            cur = cur.next

    def add(self, item):
        """从头节点插入节点"""
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """从尾节点插入节点"""
        node = Node(item)
        cur = self._head
        if self.is_empty():
            self._head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, position, item):
        """指定位置后插入元素，位置按下标=0开始计数"""
        node = Node(item)
        pre  =self._head
        count = 0
        if position <= 0:
            self.add(item)
        elif position >= self.length()-1:
            self.append(item)
        else:
            while count < (position):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        """ 针对查找的元素是第一个时"""
        if item == cur.element:
            self._head = self._head.next
            return ("remove node", cur.element)

        """ 针对查找的元素不是第一个时"""
        while cur.next != None:
            temp = cur.next.element
            if cur.next.element == item:
                cur.next = cur.next.next
                return ("remove node", temp)
            else:
                cur = cur.next
        return ("no such node", None)


    def search(self, item):
        """查找节点是否存在"""
        cur = self._head
        while cur != None:
            if cur.element == item:
                return True
            else:
                cur = cur.next
        return False


node1 = Node(100)
singleLinkList = SingleLinkList(node1)
singleLinkList.append(20)
singleLinkList.append("element")

singleLinkList.add(0)
singleLinkList.insert(2, "2+")
singleLinkList.travel()
print("\nlength:", singleLinkList.length())

print("search:", singleLinkList.search("element"))

print(singleLinkList.remove(110))
singleLinkList.travel()
print("\n")
print(singleLinkList.remove(0))
singleLinkList.travel()


