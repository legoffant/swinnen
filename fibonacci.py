#!/usr/bin/python
# -*- coding:utf-8 -*-

# Suite de fibonacci
# Chaque terme est egal a la somme des deux termes précédent

a, b, c = 1, 0, 0         # On met à zéro la variable b et le compteur c
while c < 11:             # tant que c est inférieur a 11 on compte
    a, b, c = b, a+b, c+1 # Assignation parallèle
    print(b, end=" ")