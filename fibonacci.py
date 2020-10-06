#!/usr/bin/python
# -*- coding:utf-8 -*-

a, b, c = 1, 1, 1
while c < 11:
    a, b, c = b, a+b, c+1
    print(b, end=" ")