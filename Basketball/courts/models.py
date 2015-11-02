from django.db import models

# Create your models here.
class Court(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField()
    location = models.TextField(default="")
    num_of_courts = models.IntegerField()
    accessible = models.CharField(max_length=1)
    longitude = models.TextField()
    latitude = models.TextField()

    class Meta:
        ordering = ('created', )
