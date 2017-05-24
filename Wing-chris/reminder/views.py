#!/usr/bin/env python
# coding: utf-8
u"""日程提醒."""
from django.views.decorators.csrf import csrf_exempt

from utils.response import render_response
from error import ERROR_CODE, ERROR_MESSAGE
from reminder.models import DailyList, Reminder
import datetime
import logging

logger = logging.getLogger('reminder')


@csrf_exempt
def operate_daily_list(request):
    u"""保存每日清单."""
    _id = request.POST.get("id", None)
    content = request.POST.get("content", None)
    if len(content) > 100:
        content = content[:100]
    logger.info(content)
    if not content:
        return render_response(ERROR_CODE.PARAMS, ERROR_MESSAGE.PARAMS)

    if _id:
        dy = DailyList.objects.filter(id=_id).first()
    else:
        dy = DailyList()
        dy.create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dy.is_valid = 1
    try:
        dy.content = content
        dy.update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dy.save()
    except Exception as ex:
        logger.exception(ex)

    daily_id = dy.id

    return render_response(ERROR_CODE.SUCCESS, ERROR_MESSAGE.SUCCESS, data={"id": daily_id})


def daily_index(request):
    u"""每日清单列表"""
    rows = DailyList.objects.filter(is_valid=1, status="Doing").order_by("-update_time")
    history_data = []
    today_data = []
    # 今天零点时间
    today = datetime.datetime.today()
    today_time = datetime.datetime(today.year, today.month, today.day)
    print today_time
    for row in rows:
        if row.update_time < today_time:
            history_data.append({'id': row.id, "content": row.content})
        else:
            today_data.append({"id": row.id, "content": row.content})
    data = {"history": history_data, "today": today_data}

    return render_response(ERROR_CODE.SUCCESS, ERROR_MESSAGE.SUCCESS, data=data)


def daily_modify(request):
    """daily 状态修改或删除"""

    _id = request.GET.get("id", None)
    if not _id:
        return render_response(ERROR_CODE.PARAMS, ERROR_MESSAGE.PARAMS)

    _status = request.GET.get("status", None)
    if not _status:
        return render_response(ERROR_CODE.PARAMS, ERROR_MESSAGE.PARAMS)

    row = DailyList.objects.filter(is_valid=1, id=_id).first()
    if not row:
        return render_response(ERROR_CODE.NOT_FOUND, ERROR_MESSAGE.NOT_FOUND)

    try:
        if _status == "Deleting":
            row.is_valid = 0
            row.status = _status
        elif _status == "Finish":
            row.status = _status
        else:
            row.status = _status

        row.save()
    except Exception as ex:
        logger.exception(ex)

    return render_response(ERROR_CODE.SUCCESS, ERROR_MESSAGE.SUCCESS)


def reminder_index(request):
    """长期计划 index"""
    reminder_data = []
    rows = Reminder.objects.filter(is_valid=1).order_by("-create_time")
    for row in rows:
        reminder_data.append({"id": row.id, "start_time": row.start_time, "content": row.content, "type": row.type})

    return render_response(ERROR_CODE.SUCCESS, ERROR_MESSAGE.SUCCESS, data=reminder_data)


def reminder_modify(request):
    """长期计划 修改"""

    # 1:完成，2:删除
    flag = request.POST.get("flag", None)
    _id = request.POST.get("id", None)
    if not _id or not flag:
        return render_response(ERROR_CODE.PARAMS, ERROR_MESSAGE.PARAMS)

    try:
        row = Reminder.objects.filter(id=_id).first()
        if not row:
            return render_response(ERROR_CODE.NOT_FOUND, ERROR_MESSAGE.NOT_FOUND)

        if flag == 1:
            row.status = "Finish"
        elif flag == 2:
            row.status = "Deleting"
            row.is_valid = 0

        row.save()
    except Exception as ex:
        logger.exception(ex)

    return render_response(ERROR_CODE.SUCCESS, ERROR_MESSAGE.SUCCESS)


def reminder_add_modify(request):

    _id = request.POST.get("id", None)
    content = request.POST.get("content", None)
    start_time = request.POST.get("start_time", None)
    _type = request.POST.get("type", 0)
    times = request.POST.get("times", 2)
    try:
        row = Reminder.objects.filter(id=_id).first()
        if not row:
            # 添加
            row = Reminder()
            row.create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            row.type = _type

        row.content = content
        row.start_time = start_time
        row.times = times

        row.save()
    except Exception as ex:
        logger.exception(ex)

    return render_response(ERROR_CODE.SUCCESS, ERROR_MESSAGE.SUCCESS)
