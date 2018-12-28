#! /usr/bin/env python
# encoding: utf-8
# @Time :2018/12/24 0024 下午 4:58
__Author__ = '村长'

import gitlab

def allprojects():
    #######获取gitlab的所有projects###
    projects = gl.projects.list(all=True)
    for project in projects:
        print (project.name,project.id)


if __name__ == '__main__':
    gl = gitlab.Gitlab('http://10.128.46.40/', private_token='udeR7ZU9JZ7uNzkaM7yR')
    info = {1:'allprojects()'}
    serp = '-' * 20
