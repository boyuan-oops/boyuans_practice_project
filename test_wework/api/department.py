# -*- coding: utf-8 -*-
import requests


class Department:

    def creat_department(self, token):
        create_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}"
        data = {
           "name": "广州研发中心",
           "name_en": "RDGZ",
           "parentid": 1,
           "order": 1,
           "id": 2
        }
        r = requests.post(url=create_department_url,json=data)
        return r.json()

    def update_department(self, token):
        update_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}"
        data = {
            "id": 2,
            "name": "研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.post(url=update_department_url, json=data)
        return r.json()

    def delete_department(self, token, department_id):
        delete_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id={department_id}"
        r = requests.get(url=delete_department_url)
        return r.json()

    def get_department_list(self, token, department_id):
        department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}&id={department_id}"
        r = requests.get(url=department_list_url)
        return r.json()
