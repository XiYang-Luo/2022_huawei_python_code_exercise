"""
假设在平面直角坐标系（上北-Y轴正方向，下南-Y轴负方向，左西-X轴负方向，右东-X轴正方向）上，一个遥控小车最初位于原点 (0, 0) 处，且面朝北方。

遥控小车可以接受下列三条指令之一：
“G”：直走 1 个单位
“L”：左转 90 度
“R”：右转 90 度

给定一批指令，遥控小车按顺序执行每个指令后，请计算遥控小车最终所处的位置。

用例保证整个过程中坐标(x,y)的值都在 int (32 位系统)范围内

解答要求
时间限制：1000ms, 内存限制：64MB
输入
字符串表示的一批遥控指令，仅由字符 G、L、R组成，长度范围[1,100]

输出
小车最终所处位置的坐标

样例
输入样例 1 复制

GG
输出样例 1

(0,2)
提示样例 1
"""


import itertools
import math
import operator
import random
import re
import string
import sys
import json

"""
Copyright (c) Huawei Technologies Co., Ltd. 2020-2020. All rights reserved.
Description: 上机编程认证
Note: 缺省代码仅供参考，可自行决定使用、修改或删除
"""


"""
x += 1 和 x = x+1
首先python中变量名是变量的标签，因此重新赋值在某种意义上是标签的重新指向，而在a += 1和a = a + 1两个问题上，更准确是说是对于不可变对象类型，
是重新开辟空间，这个标签指向新的内存空间，对于可变对象类型，则是在原来内存上做操作。

简言之：

对于可变对象，a += 1 直接在原内存地址上操作a = a + 1开辟新的内存操作
对于不可变对象，a += 1和a = a + 1都是在新开辟的空间操作
————————————————
版权声明：本文为CSDN博主「Snfiltration」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_34159047/article/details/109229108
"""
class Solution:
    def exec_command(self, commands):
        # 在此添加你的代码
        x, y = 0, 0
        # 方向: 0上   1右   2下   3左
        dir = 0
        for item in commands:
            if item == "G":
                if dir == 0:
                    y = y + 1
                if dir == 1:
                    x = x + 1
                if dir == 2:
                    y -= 1
                if dir == 3:
                    x = x - 1
            if item == "L":
                if dir == 0:
                    dir = 3
                else:
                    dir -= 1

            if item == "R":
                if dir == 3:
                    dir = 0
                else:
                    dir = dir + 1
        return [x, y]


if __name__ == "__main__":
    commands = str(input().strip())
    function = Solution()
    results = function.exec_command(commands)
    print("(" + str.join(",", map(str, results)) + ")")
