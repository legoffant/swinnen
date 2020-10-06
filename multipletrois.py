#!/usr/bin/python
# -*- coding:utf-8 -*-

n = 1
while n < 21:
    t = n * 7
    print(t, end=" ")
    if t % 3 == 0:
        print("*", end=" ")
    
    n += 1
    