#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')
print(2)

a= 10
b= '22.5'
d= '20'

print("type of a before convert",type(a))
print("type of a before convert", type(b))
print("type of a before convert", type(d))
# b = float(b)
# print("type of a before convert", type(b))
# b = int(b)

d = int(d,3)
print(d)
c= a + int(float(b))
print(c)
print("the type of c is", type(c))

w = None
print("The type of w is:",type(w))
w =c
print(c)
#
# ord()
# hex()
# oct()
# eval()

