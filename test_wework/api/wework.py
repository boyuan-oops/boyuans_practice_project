# -*- coding: utf-8 -*-
import requests


class WeWork():

    def get_token(self):
        corpid = "ww9902a7f431a1e2c5"
        corpsecret = "t3U8xhf3XKI92WfHc8gROg91V4KuPgPrtW1pET-Wio0"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=token_url)
        return r.json()["access_token"]