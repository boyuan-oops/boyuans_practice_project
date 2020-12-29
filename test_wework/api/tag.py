# -*- coding: utf-8 -*-
import requests


class Tag:

    def create_tag(self, token):
        create_tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}"
        data = {
           "tagname": "UI",
           "tagid": 12
        }
        r = requests.post(url=create_tag_url, json=data)
        return r.json()

    def update_tag(self,token):
        update_tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}"
        data = {
           "tagid": 12,
           "tagname": "UI design"
        }
        r = requests.post(url=update_tag_url, json=data)
        return r.json()

    def delete_tag(self, token):
        delete_tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}&tagid=12"
        r = requests.get(url=delete_tag_url)
        return r.json()

    def get_tag_list(self, token):
        tag_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}"
        r = requests.get(url=tag_list_url)
        return r.json()
