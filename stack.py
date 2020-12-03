#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""栈表"""


class Stack(object):
    def __init__(self):
        self.items = list()

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()

    def peek(self):
        """
        返回栈顶项但不删除
        :return:
        """
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)