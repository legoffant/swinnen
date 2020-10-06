#!/usr/bin/python
# -*- coding:utf-8 -*-

nombre = 374083219 # seconde a convertir

cm = nombre // 60
cs = nombre % 60

ch = cm // 60
cm = cm % 60

ca = ch // 24
ch = ch % 24

print(ca, ":",ch, ":",cm, ":",cs)
