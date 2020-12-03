#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""链表实现:
节点组成：数据项， 下一项地址信息
add()：从表头开始插入算法复杂度最低，所以插入时，越先插入，在链表中的位置越靠后
search()
pop()
remove()
is_empty()

"""

class Node(object):
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next_info):
        self.next = next_info


class UnOrderedList(object):
    def __init__(self):
        """设立一个head，保存对一个节点的引用，空表的head为None"""
        self.head = None

    def add(self, item):
        """ None --> data|next --> data|next"""
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def pop(self):
        pass

    def search(self):
        pass

    def remove(self):
        pass

    def is_empty(self):
        return self.head is None

    def size(self):
        pass



class OrderedList(object):
    """
    有序表： 数据项依照某种可比性来决定在列表中的位置
    """
    def __init__(self):
        self.head = None

    def add(self, item):
        """保证列表的有序性"""
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                current = self.get_next()
        # TODO 插入操作

    def pop(self):
        pass

    def search(self, item):
        """有序链表： 中间某项大于查询值得时候即可结束"""
        current = self.head
        found = False
        stop = False
        while current is not None and  not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def remove(self):
        pass

    def is_empty(self):
        """O(1): 检查head是否为None"""
        pass

    def size(self):
        """O(n): 表头到表尾"""
        pass

    def get_data(self):
        return

    def get_next(self):
        return


if __name__ == '__main__':
    tmp = Node(90)
    print(tmp.get_data())

