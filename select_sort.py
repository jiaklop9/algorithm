#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
冒泡排序基础上，比对次数不变，记录最大数，最后一次交换
O(n)
"""

def main(data_list):
    for index in range(len(data_list)-1, 0, -1):
        max_data = 0
        for i in range(1, index+1):
            if data_list[i] > data_list[max_data]:
                max_data = i
        tmp = data_list[index]
        data_list[index] = data_list[max_data]
        data_list[max_data] = tmp

    return data_list


if __name__ == '__main__':
    data = [1,45,78,0, 92, 103]
    print(main(data))
