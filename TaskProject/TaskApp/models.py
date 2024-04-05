from django.db import models

# Create your models here.
class Tasks(models.Model):
    title=models.CharField(max_length=256)
    description=models.CharField(max_length=500, blank=True)
    status=models.CharField(max_length=100)

    class Meta:
        app_label = 'TaskApp'
        db_table = 'tasks'
        default_related_name = 'tasks'