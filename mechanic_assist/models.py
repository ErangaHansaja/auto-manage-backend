from django.db import models

# Create your models here.
class AssistRequest(models.Model):
    customer_id = models.IntegerField()
    vehicle_id = models.IntegerField()
    issue = models.TextField()

class Summary(models.Model):
    service_id = models.IntegerField()
    service_summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
