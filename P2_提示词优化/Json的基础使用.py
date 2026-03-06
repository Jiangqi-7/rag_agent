# -*- coding: UTF-8 -*-
"""
@Project ：PycharmProjects 
@File    ：Json的基础使用.py
@Author  ：九成八
@Date    ：2026/3/6 01:06 
"""
import json

d = {
    "name": "九成八",
    "age": 18,
    "gender": "male"
}

l = [
    {
        "name": "九成八",
        "age": 18,
        "gender": "male"
    },
    {
        "name": "九成九",
        "age": 19,
        "gender": "male"
    }, {
        "name": "十成",
        "age": 20,
        "gender": "male"
    }
]

# 字典转json字符串
s = json.dumps(d, ensure_ascii=False)
print(s)
print(json.dumps(l, ensure_ascii=False))

json_str = '{"name": "九成八", "age": 18, "gender": "male"}'
json_arr_str = '[{"name": "九成八", "age": 18, "gender": "male"}, {"name": "九成九", "age": 19, "gender": "male"}, {"name": "十成", "age": 20, "gender": "male"}]'

# json字符串转python字典
res_dict = json.loads(json_str)
print(res_dict,type(res_dict))

res_list = json.loads(json_arr_str)
print(res_list,type(res_list))
