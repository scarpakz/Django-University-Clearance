from django.db import models
from django.contrib.auth.models import User

class ClearanceStatus(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{},{}".format(self.user, self.status)

class Clearance(models.Model):
    student = models.ForeignKey(User, on_delete = models.CASCADE)
    dean = models.ForeignKey(ClearanceStatus, related_name="dean", on_delete = models.CASCADE, default=None)
    chairman = models.ForeignKey(ClearanceStatus, related_name="chairman", on_delete = models.CASCADE, default=None)
    assessment = models.ForeignKey(ClearanceStatus, related_name="assessment", on_delete = models.CASCADE, default=None)
    request = models.IntegerField(default=0)

    def __str__(self):
        return "{},{},{}".format(self.dean, self.chairman, self.assessment)