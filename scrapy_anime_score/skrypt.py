#!/usr/bin/python3
import sys

list = []
word = []

for line in sys.stdin:
    list.append(line.replace('\"', '\''))

list2 = []

for i in list:
    list2.append(i.replace('\\\'', '\"'))

list3 = []

for i in list2:
    list3.append(i.replace(',', ''))

for i in list3:
    print(i[:-1])