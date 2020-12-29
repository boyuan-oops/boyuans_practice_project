# -*- coding: utf-8 -*-
from test_wework.api.tag import Tag
from test_wework.api.wework import WeWork


class TestTag():

    def setup_class(self):
        wework = WeWork()
        self.token = wework.get_token()
        self.tag = Tag()

    def test_create_tag(self):
        r = self.tag.create_tag(self.token)
        taglist = self.tag.get_tag_list(self.token)
        print(taglist)
        assert taglist["taglist"][0]["tagid"] == 12

    def test_update_tag(self):
        r = self.tag.update_tag(self.token)
        taglist = self.tag.get_tag_list(self.token)
        assert taglist["taglist"][0]["tagname"] == "UI design"

    def test_delete_tag(self):
        r = self.tag.delete_tag(self.token)
        taglist = self.tag.get_tag_list(self.token)
        print(taglist)
        assert len(taglist["taglist"]) == 0