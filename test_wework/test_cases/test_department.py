# -*- coding: utf-8 -*-
from test_wework.api.department import Department
from test_wework.api.wework import WeWork


class TestDepartment():

    def setup_class(self):
        wework = WeWork()
        self.token = wework.get_token()
        self.department = Department()


    def test_create_department(self):
        r = self.department.creat_department(self.token)
        assert r["errcode"] == 0

    def test_update_department(self):
        r = self.department.update_department(self.token)
        assert r["errmsg"] == "updated"

    def test_delete_department(self):
        r = self.department.delete_department(self.token, 2)
        assert r["errmsg"] == "deleted"

