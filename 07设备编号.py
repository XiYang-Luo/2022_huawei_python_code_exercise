'''
题目描述
给定一个设备编号区间[start, end]，包含4或18的编号都不能使用，如：418、148、718不能使用，108可用。

请问有多少可用设备编号。

解答要求
时间限制：1000ms, 内存限制：256MB
输入
两个整数start end(单空格间隔)，用于标识设备编号区间，0 < start < end <= 100000

输出
一个整数，代表可用设备编号的数量

样例
输入样例 1 复制

3 20
输出样例 1

15
提示样例 1
不能使用的设备编号为4、14、18



输入样例 2 复制

1 1000
输出样例 2

711
提示样例 2
 '''


class Solution:
    def get_normal_device_number(self, start, end):
        count = 0
        r = []
        for item in range(start, end+1, 1):
            item_str = str(item)
            if "4" in item_str or "18" in item_str:
                r.append(item)
            else:
                count = count + 1
        print(r)
        return count


if __name__ == "__main__":
    start, end = tuple(map(int, input().strip().split()))
    function = Solution()
    result = function.get_normal_device_number(start, end)
    print(result)
