from django.db import models
from form.models import Clearance, ClearanceStatus
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user_type = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    