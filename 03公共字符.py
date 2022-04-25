# -*- coding:utf-8 -*-
"""
作者：xiyang
日期：2022年04月25日
功能解释：
    https://ilearningx.huawei.com/portal/oj/problems/3/details
    给定 m 个字符串，请计算有哪些字符在所有字符串中都出现过 n 次及以上。

    解答要求
    时间限制：1000ms, 内存限制：256MB
    输入
    首行是整数 n ，取值范围 [1,100]
    第二行是整数 m ，表示字符串的个数，取值范围 [1,100]
    接下来 m 行，每行一个仅由英文字母和数字组成的字符串，长度范围 [1,1000)

    输出
    按ASCII码升序输出所有符合要求的字符序列； 如果没有符合要求的字符，则输出空序列[]。

    样例
    输入样例 1 复制

    2
    3
    aabbccFFFFx2x2
    aaccddFFFFx2x2
    aabcdFFFFx2x2
    输出样例 1

    [2 F a x]
    提示样例 1


    输入样例 2 复制

    2 3
    aa
    bb
    cc
    输出样例 2

    []
"""


class Solution:
    def get_n_times_character(self, n_value, strings):
        # 在此添加你的代码
        print(n_value, strings)
        str_map = dict()
        for index, item in enumerate(strings):
            for s_index, s_item in enumerate(item):
                if str_map.__contains__(s_item):
                    c = str_map[s_item]["count"] + 1
                    li = str_map[s_item]["list_index"]
                    li.append(index)
                    str_map[s_item] = {"count": c, "list_index": li}
                else:
                    str_map[s_item] = {"count": 1, "list_index": [index], }
        print(str_map)

        res = []
        for k, v in str_map.items():
            count = v["count"]
            list_index =list(v["list_index"])
            # 先判断a出现的次数是否多余 n*m （按照每个字符串中出现的达标的最小次数计算）
            if count >= n_value * len(strings):
                # 判断 是否在每一个字符串中都出现，如果不是，则不达标
                if len(list(set(list_index))) >= len(strings):
                    dic_list_index = dict()
                    # 获取每一个字符在各个字符串中出现的次数
                    for item in list_index:
                        if dic_list_index.__contains__(item):
                            # 对于次数已经达标的字符不再计数
                            if dic_list_index[item] < n_value:
                                dic_list_index[item] += 1
                        else:
                            dic_list_index[item] = 1
                    print(dic_list_index)
                    x = list(set(dic_list_index.values()))
                    print(x)
                    # 如果该字符在每一个字符串中均出现，并且出现次数达标，则该字符保存在最终结果中
                    if len(x) == 1 and x[0] == n_value:
                        res.append(k)
                    else:
                        pass
                else:
                    pass
            else:
                pass
        res.sort()
        return res


if __name__ == "__main__":
    # n_value = int(input().strip())
    # num = int(input().strip())
    # strings = [input().strip() for _ in range(num)]
    n_value = 2
    num = 3
    strings = ["aabbccFFFFx2x2", "aaccddFFFFx2x2", "aabcdFFFFx2x2"]
    # strings = ["aa", "bb", "cc"]

    function = Solution()
    results = function.get_n_times_character(n_value, strings)
    print("[" + str.join(" ", map(str, results)) + "]")
