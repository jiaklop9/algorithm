#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
递归： 将问题分解成更小的规模的相同问题
"""

def sum_list(data_list):
    result = 0
    for i in data_list:
        result += i
    return result

"""
假设不能用for和while的话
"""
"""
递归三定律：
    必须有结束条件
    必须能改变自身向更小规模转换
    必须调用自身
"""
def _recursion(data_list):
    if len(data_list) == 1:
        return data_list[0]
    else:
        return data_list[0] + _recursion(data_list[1:])


"""
样例： 进制转换（取余）
"""

def base_conversion(data, base):
    convert_string = '0123456789ABCDEF'
    if data < base:
        return convert_string[data]
    else:
        return base_conversion(data // base, base) + convert_string[data % base]


if __name__ == '__main__':
    print(base_conversion(25, 16))