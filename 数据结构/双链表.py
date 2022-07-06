class Node(object):
    """ 节点 类"""
    def __init__(self, element):
        # 元素值
        self.element = element
        # 前驱节点地址
        self.pre = None
        # 后继节点地址
        self.next = None

class DoubleLinkList(object):
    """ 双链表 类"""
    def __init__(self, node=None):
        self. _head = Node(node)

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
        """遍历双链表"""
        cur = self._head
        while cur != None:
            print(cur.element, end=" ")
            cur = cur.next

    def add(self, item):
        """从头节点插入节点"""
        node = Node(item)
        node.next = self._head
        self._head = node
        node.next.pre = node

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
            node.pre = cur

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
            cur = self._head
            while count < (position+1):
                count += 1
                cur = cur.next
            node.next = cur
            node.pre = cur.pre
            cur.pre.next = node
            cur.pre = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        """ 针对查找的元素是第一个时"""
        if item == cur.element:
            self._head = self._head.next
            if cur.next is not None:
                self._head.next.pre = None
            return ("remove node", cur.element)

        """ 针对查找的元素不是第一个时"""
        while cur != None:
            temp = cur.element
            if cur.element == item:
                cur.pre.next = cur.next
                if cur.next is not None:
                    cur.next.pre = cur.pre
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

# node1 = Node(100)
doubleLinkList = DoubleLinkList(100)
doubleLinkList.append(20)
doubleLinkList.append("element")

doubleLinkList.add(0)
doubleLinkList.insert(2, "2+")
doubleLinkList.travel()
print("\nlength:", doubleLinkList.length())

print("search:", doubleLinkList.search("element"))

print("--------------")
print(doubleLinkList.remove(110))
doubleLinkList.travel()

print("\n")
print(doubleLinkList.remove("element"))
doubleLinkList.travel()
