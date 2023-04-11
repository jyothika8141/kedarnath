from django.db import models
from django.contrib.auth.models import User


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(null=True, blank=True)
    check_in_message = models.CharField(max_length=500, null=True, blank=True)
    check_out_message = models.CharField(max_length=500, null=True, blank=True)

    def to_dict(self):
        return {
            "user": self.user.username,
            "check_in": self.check_in,
            "check_out": self.check_out,
            "check_in_message": self.check_in_message,
            "check_out_message": self.check_out_message,
        }


class LeaveRequest(models.Model):
    status_choices = (
        ("pending", "pending"),
        ("approved", "approved"),
        ("rejected", "rejected"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=500)
    status = models.CharField(choices=status_choices, max_length=50, default="pending")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def to_dict(self):
        return {
            "user": self.user.username,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "reason": self.reason,
            "status": self.status,
        }