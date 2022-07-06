class Node(object):
    """ 节点 类"""
    def __init__(self, element):
        # 元素值
        self.element = element
        # 后继节点地址
        self.next = None

class SingleCycleLinkList(object):
    """ 单向循环链表 """
    def __init__(self, element):
        node = Node(element)
        self.__head = node
        # self.__head.next = self.__head
        node.next = node

    def is_empty(self):
        """判断是否为空"""
        return self.__head == None

    def length(self):
        """长度"""
        cur = self.__head
        if cur is None:
            return 0
        count = 1
        while cur.next != self.__head:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历单链表"""
        cur = self.__head
        if self.is_empty():
            print("空的链表")
            return
        while cur.next != self.__head:
            print(cur.element, end=" ")
            cur = cur.next
        # 退出循环时， cur指向尾节点，但是未打印元素
        print(cur.element)

    def add(self, item):
        """从头节点插入节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        # 退出循环，cur指向最后一个节点
        node.next = self.__head
        self.__head = node
        cur.next = node # 最后一个节点的next 指向头节点

    def append(self, item):
        """从尾节点插入节点"""
        node = Node(item)
        cur = self.__head
        # 如果链表为空
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, position, item):
        """指定位置后插入元素，位置按下标=0开始计数"""
        node = Node(item)
        pre  =self.__head
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
        if self.is_empty():
            return ("no such node", None)
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            temp = cur.element
            if cur.element == item:
                """ 针对查找的元素是第一个时  头节点"""
                if cur == self.__head:
                    cur1 = self.__head
                    while cur1.next != self.__head:
                        cur1 = cur1.next
                    self.__head = cur.next
                    cur1.next = self.__head
                    return ("remove node", cur.element)
                else:
                    """ 针对查找的元素不是第一个时 中间节点"""
                    pre.next = cur.next
                    return ("remove node", temp)
            else:
                pre = cur
                cur = cur.next
        # 尾节点
        if cur.element == item:
            if pre is not None:
                pre.next = self.__head
                return ("remove node", cur.element)
            else:
                # 链表只有一个节点
                self.__head = None
                return ("remove node", cur.element)
        return ("no such node", None)


    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        if cur is None:
            return False
        else:
            # 判断第一个节点是否是要查找的元素
            if cur.element == item:
                return True

        # 判断第一个节点之后，是否存在要查找的元素
        while cur.next != self.__head:
            if cur.next.element == item:
                return True
            else:
                cur = cur.next
        # 对最后一个节点的判断
        if cur.element == item:
            return True
        return False



node1 = Node(100)
singleCycleLinkList = SingleCycleLinkList(100)
singleCycleLinkList.append(20)
singleCycleLinkList.append("element")

singleCycleLinkList.add(0)
singleCycleLinkList.insert(2, "2+")
singleCycleLinkList.travel()
print("\nlength:", singleCycleLinkList.length())

print("search:", singleCycleLinkList.search(0))

print(singleCycleLinkList.remove(110))
singleCycleLinkList.travel()

print("----------\n")
print(singleCycleLinkList.remove("element"))
singleCycleLinkList.travel()
