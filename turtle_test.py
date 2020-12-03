#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""程序作图"""

import time
import turtle



if __name__ == '__main__':
    t = turtle.Turtle()
    for i in range(4):
        t.forward(100)
        t.right(90)
    time.sleep(10)
    t.down()


