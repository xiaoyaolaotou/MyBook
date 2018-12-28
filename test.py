#! /usr/bin/env python
# encoding: utf-8
# @Time :2018/12/25 0025 上午 10:00
__Author__ = '村长'

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

response = requests.get('http://10.128.46.40/api/v3/groups/osCloud', headers=headers)
lst = str(response.content,encoding='utf-8')
lst_3 = json.loads(lst)
# print(lst_3)
# print(lst_3['projects'][0]['name'])
for i in lst_3['projects'][0]['name']:
    groups.append(i)

print(groups)
print(len(groups))






