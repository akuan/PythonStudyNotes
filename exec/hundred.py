# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:46:51 2020

@author: Administrator
"""

def sumToHundred():
    n=100
    sum=0
    counter=1
    while counter<=n:
        sum+=counter
        counter+=1
    print(" 1 到 %d 之和为：%d"%(n,sum))

def suf(n): 
    t=0
    for x in range(n+1):
        t+=x
    print(" 1 到 %d 之和为：%d"%(n,t))

def elTest():
    var = 10                    # 第二个实例
    while var > 0:              
        var = var -1         
        if var == 5:             # 变量为 5 时跳过输出
          break         
        print ('当前变量值 :', var)
    else:
        print("else 被执行了")
    print ("Good bye!")

def ffTest():
    sites = ["Baidu", "Google","Taobao"]
    for site in sites:
        if site == "Runoob":
            print("菜鸟教程!")
            break
        print("循环数据 " + site)
    else:
        print("没有循环数据!")
    print("完成循环!")