# !/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import requests


def parse_tkl(sign_server, password):
    headers = {
        "content-type": "application/json;charset=utf-8"
    }
    payload = {
        "password": password
    }
    print("解析淘口令参数:" + json.dumps(payload))
    res = requests.post(sign_server, data=json.dumps(payload), headers=headers)
    res_content = res.text
    print("解析淘口令返回:" + str(res_content))
    ret = {}
    if res.status_code == requests.codes.ok:
        ret = json.loads(res_content)
    return ret


if __name__ == '__main__':
    tkl_server = "http://localhost:6088/"
    password = "￥chKl2FHtfTO￥"
    tkl = parse_tkl(tkl_server, password)
    print('validDate:' + tkl['validDate'])
    print('content:' + tkl['content'])
    print('title:' + tkl['title'])
    print('url:' + tkl['url'])
    print('taopwdOwnerId:' + str(tkl['taopwdOwnerId']))
