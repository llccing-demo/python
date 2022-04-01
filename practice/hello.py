#!/usr/bin/python3

# comment

'''
comment
comment
'''

"""
comment
"""
import sys
from sys import argv, path
print('Hello, World!')


# 缩进
if True:
    print("True")
    print('True2222')
else:
    print("False")


# 多行语句
item_one = "item_one "
item_two = "item_two "
item_three = "item_three"
total = item_one + \
    item_two + \
    item_three

print(total)

total = ['item_1', 'item_2', 'item_3']
print(total)


# 数字 Number 类型
'''
python 中数字有4种类型, int 整数, bool, float 浮点数, complex 复数
'''

# String
"""
' " 单引号 双引号 完全相同

\''' \""" 可以指定多行字符串


"this" "is" "a" "test" 会自动拼接到一起

字符串索引, 左到右 0 开始，右到左 -1 开始

字符串不能改变

没有字符类型，一个字符就是长度为1的字符串

字符串截取语法 变量[头下标:尾下标:步长]
"""
str = "this" "is" "a" "test"
print(str)

strTest = '123456789'
print(strTest)
print(strTest[0:-1])
print(strTest[0])
print(strTest[2:5])
print(strTest[2:])
print(strTest[1:5:2])
print(strTest*2)
print(strTest + '你好')

print('---------------------------')

# 空行
# 函数间或类的方法之间用空行分隔

# 等待用户输入
input("\n\n按下 enter 键后退出")

# 同一行展示多条语句 用分号;
x = 'runoob'
sys.stdout.write(x + '\n')

# 代码组
# 就是代码块，没有括号，就挨着写一起。

# import 与 from ... import
'''
整个模块导入
import

导入指定函数
from somemodule import somefunction

导入多个函数
from somemodule import somef1, somef2, somef3

导入模块所有函数
from somemodule import *
'''
print('================python from import===================')
print('path', path)
