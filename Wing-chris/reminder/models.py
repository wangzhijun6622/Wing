#!/usr/bin/env python
# coding: utf-8
u"""日程提醒."""

from django.db import models
import datetime

STATUS = (('Finish', 'Finish'), ('Doing', 'Doing'), ('Deleting', 'Deleting'))


class DailyList(models.Model):
    u"""每日清单model."""

    status = models.CharField("清单状态", choices=STATUS, default='Doing', max_length=36)
    content = models.TextField(max_length=100)
    create_time = models.DateTimeField(default=datetime.datetime.now)
    is_valid = models.BooleanField(default=True)
    update_time = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'daily_list'


class Reminder(models.Model):
    u"""事件提醒、长期计划model."""

    REMINDER_TYPE = ((0, '事件提醒'), (1, '长期计划'))
    start_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    type = models.SmallIntegerField('提醒类型', choices=REMINDER_TYPE, default=0)
    times = models.IntegerField(default=2)
    content = models.CharField(max_length=1024)
    is_valid = models.BooleanField(default=True)
    status = models.CharField("长期计划状态", choices=STATUS, default="Doing", max_length=36)

    class Meta:
        db_table = 'reminder'