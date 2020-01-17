# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:47:24 2020

@author: Administrator
"""

def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*,arg):
    print(arg)

def combined_example(pos_only,/,standard,*,kwd_only):
    print(pos_only,standard,kwd_only)