from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50)
    date = models.DateField(null=True)
    value = models.IntegerField()
    unit = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
