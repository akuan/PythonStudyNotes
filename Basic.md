python 基础知识
-------------------------
资源路径  
极客帮课程 https://time.geekbang.org/column/article/94929  
runoob  https://www.runoob.com/python3/python3-tutorial.html   

### dir ##
```python
dir()  
dir(__builtin__)
```

| 函数                 | 描述                                                         |
| -------------------- | ------------------------------------------------------------ |
| int(x[,base])        | 将x转换为一个整数                                            |
| float(x)             | 将x转换到一个浮点数                                          |
| complex(real[,imag]) | 创建一个复数                                                 |
| str(x)               | 将对象x转化为表达式字符串                                    |
| repr(x)              | 将对象 x 转换为表达式字符串                                  |
| eval(str)            | 用来计算在字符串中的有效Python表达式,并返回一个对象          |
| tuple(s)             | 将序列 s 转换为一个元组                                      |
| list(s)              | 将序列 s 转换为一个列表                                      |
| set(s)               | 转换为可变集合                                               |
| dict(d)              | 创建一个字典。d 必须是一个 (key, value)元组序列。            |
| frozenset(s)         | 转换为不可变集合                                             |
| chr(x)               | 将一个整数转换为一个字符                                     |
| ord(x)               | 将一个字符转换为他的整数值;**例子**dict(zip([i for i in range(100)],[chr(i) for i in range(100)])) |
| zip(x)               | **zip()** 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表 |
| hex(x)               | 将一个整数转换为一个十六进制字符串                           |
| oct(x)               | 将一个整数转换为一个八进制字符串                    |

 函数返回多个值的时候，是以元组的方式返回的 ；

 函数变长参数，比如以 "*" 开头的的参数名会将所有的参数收集到一个元组上  

  type 不认为子类是父类的一种类型，而isinstance会认为子类是父类的一种类型。 

 获取 dict 的键值对，可直接用 **items()** 函数： for k,v in dict.items()

成员运算符 in,not in  

身份运算符is ,is not: if(a is b): #判断是否有相同的地址， 类似 **id(x) == id(y)**  

 **is** 用于判断两个变量引用对象是否为同一个， **==** 用于判断引用变量的值是否相等 

对于列表 b=a 则有 id(a)=id(b);b=a[:] 则id(a)!=id(b)

if ... :

elif...:

else:

python 无switch/case语句，可以使用字典来替代。

无do...while循环

 在 python 中，while … else 在循环条件为 false 时执行 else 语句块 

## 数据类型

### string

1. 字符串可以用+运算符连接在一起，用*运算符重复。  
2. 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。  
3. Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。

### 列表与元组

1. []表示列表,()表示元组,列表元素可修改，元组不可修改

### 集合

创建集合 ：{ } 或者 set() 函数  
字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

## 运算符

//	取整除 - 向下取接近除数的整数  
:=	海象运算符，可在表达式内部为变量赋值。  
位运算符同其他语言,逻辑运算符使用 and or not  
成员运算符 in,not in;测试实例中包含了一系列的成员，包括字符串，列表或元组  
身份运算符:  
is 是判断两个标识符是不是引用自一个对象
is not 是判断两个标识符是不是引用自不同对象
 id()  函数用于获取变量内存地址
异同： is 是否同一对象，==对象值是否相等
del 语句删除变量
[ : ] 左闭右开原则
f-string 同于c# $ 

mark  https://www.runoob.com/python3/python3-string.html 