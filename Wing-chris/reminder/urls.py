#!/usr/bin/env python
# coding: utf-8
"""
@author: jian.jiao.

@time: 2016/12/16 13:29
"""
from django.conf.urls import url
from reminder import views

urlpatterns = [
    url(r'^daily/save/?$', views.operate_daily_list),
    url(r'^daily/index/?$', views.daily_index),
    url(r'^daily/modify/?$', views.daily_modify),

    url(r'^reminder/save/?$', views.reminder_add_modify),
    url(r'^reminder/modify/?$', views.reminder_modify),
    url(r'^reminder/index/?$', views.reminder_index),
]
