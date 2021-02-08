#!/usr/bin/python

base10_string = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
flag = base10_string.to_bytes(33, "big")

print("The flag is :{}".format(flag))
