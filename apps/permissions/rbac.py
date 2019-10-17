#!usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
import re

class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class Middle(MiddlewareMixin):
    def process_request(self, request):
        current_url = request.path_info

        for url in settings.WHITE_LIST:
            if re.match(url, current_url):
                return None
        permission_dict = request.session.get(settings.PERMISSION_URL_DICT)
        if not permission_dict:
            return redirect("/login/")

        flag = False
        for group_id, code_url in permission_dict.items():
            for db_url in code_url["urls"]:
                regex = "^{0}$".format(db_url)

                if re.match(regex, current_url):
                    request.permission_code_url = code_url["code"]
                    flag = True
                    break
            if flag:
                break
        if not flag:
            return redirect('/403.html')

    def process_reponse(self, request, response):
        return response
