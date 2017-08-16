#!/usr/bin/python
#coding:utf8


import requests

class request(object):
    def __init__(self):
        self.name = "qiukai"
        self.sex = "body"
    @classmethod
    def doing(cls):
        do = requests.get("http://www.baidu.com")
        print do.text

request.doing()
