#! /usr/bin/env python
# encoding: utf-8
# @Time :2018/12/24 0024 下午 3:17
__Author__ = '村长'

import requests
# import gitlab
#
#
# url = "http://10.128.46.40/api/v4/groups/"
#
# url2 = "http://code.gome.inc/gitlab/api/v3/groups/"
# private_token = "udeR7ZU9JZ7uNzkaM7yR"
#
#
# r = requests.get(url)
# print(r.text)

import requests
import json
headers = {
    'PRIVATE-TOKEN': 'udeR7ZU9JZ7uNzkaM7yR',
}
groups = []
# for i in range(1,5):
#     response = requests.get(f'http://10.128.46.40/api/v3/groups/?page{i}', headers=headers)
#     lst = str(response.content,encoding='utf-8')
#     lst_3 = json.loads(lst)
#     print(lst_3)
#     for i in lst_3:
#         groups.append(i["name"])
# #
# print(groups)
# print(len(groups))


response = requests.get(f'http://1.1.1.1.1/api/v3/groups/?per_page=100', headers=headers)
lst = str(response.content,encoding='utf-8')
lst_3 = json.loads(lst)
print(lst_3)
for i in lst_3:
    groups.append(i["name"])
#
print(groups)
print(len(groups))







