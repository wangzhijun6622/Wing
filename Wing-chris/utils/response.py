#!/usr/bin/python
# coding: utf-8
u"""
Create on 2017-01-11.

@author: jian.jiao
"""
from django.http.response import JsonResponse


def render_response(code, message=None, data={}):
    u"""Render Wing Response Data."""
    extra = {"code": code, }
    if message:
        extra.update({"message": message})
    if data:
        extra.update({"data": data})

    return JsonResponse(data=extra)