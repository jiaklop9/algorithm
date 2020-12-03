#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""冒泡排序：每次选出最大数值，共n-1次排序
n-1 + n-2 + n-3 + ... + 1  --> 1/2n^2 + 1/2n  --> O(n^2)
"""

def main(data_list):
    for index in range(len(data_list) - 1, 0, -1):
        for i in range(index):
            if data_list[i] > data_list[i+1]:
                data_list[i+1], data_list[i] = data_list[i], data_list[i+1]
    return data_list


if __name__ == '__main__':
    data = [1,45,78,0, 92, 103]
    print(main(data))