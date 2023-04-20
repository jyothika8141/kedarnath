from django.contrib import admin

from .models import Attendance, LeaveRequest, Reimbursement, Profile

admin.site.register(Attendance)
admin.site.register(LeaveRequest)
admin.site.register(Reimbursement)
admin.site.register(Profile)