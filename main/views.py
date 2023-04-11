import datetime
import json

from main.models import Attendance, LeaveRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import date


@csrf_exempt
def check_in(request):

    try:
        user = request.user
        print(user)
        req = request.POST
        check_in_message = req["check_in_message"]
        attendance = Attendance.objects.create(user=user, check_in_message=check_in_message)
        return JsonResponse({"status": 200, "data": attendance.to_dict()})
    except Exception as e:
        print(e)
        return JsonResponse({"status": 500, "message": "Something went wrong"})


@csrf_exempt
def check_out(request):
    try:
        user = request.user
        req = request.POST
        check_out_message = req["check_out_message"]
        attendance = Attendance.objects.filter(user=user).last()
        attendance.check_out = datetime.datetime.now()
        attendance.check_out_message = check_out_message
        attendance.save()
        return JsonResponse({"status": 200, "data": attendance.to_dict()})
    except Exception as e:
        print(e)
        return JsonResponse({"status": 500, "message": "Something went wrong"})


@csrf_exempt
def check_attendance(request):
    user = request.user
    print(user.username)
    attendance = Attendance.objects.filter(user=user).last()
    print(attendance.check_in.date())
    print(date.today())
    if attendance is None or attendance.check_in.date() != date.today():
        return JsonResponse({"status": 200, "data": None})
    return JsonResponse({"status": 200, "data": attendance.to_dict()})


@csrf_exempt
def submit_leave_request(request):
    try:
        user = request.user
        req = json.loads(request.body)
        print(req)
        start_date = req["start_date"]
        end_date = req["end_date"]
        reason = req["reason"]
        start_date = date(start_date["from"]["year"], start_date["from"]["month"], start_date["from"]["day"])
        end_date = date(end_date["to"]["year"], end_date["to"]["month"], end_date["to"]["day"])
        leave_request = LeaveRequest.objects.create(user=user, start_date=start_date, end_date=end_date, reason=reason)
        return JsonResponse({"status": 200, "data": leave_request.to_dict()})
    except Exception as e:
        print(e)
        return JsonResponse({"status": 500, "message": "Something went wrong"})


@csrf_exempt
def get_leave_requests(request):
    user = request.user
    leave_requests = LeaveRequest.objects.filter(user=user).order_by("-created_at")
    if leave_requests is None:
        return JsonResponse({"status": 200, "data": []})
    leave_requests = [leave_request.to_dict() for leave_request in leave_requests]
    return JsonResponse({"status": 200, "data": leave_requests})
