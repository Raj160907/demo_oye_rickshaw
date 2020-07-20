from django.db import models
from .models import *
# Create your models here.
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model
User = get_user_model()

class UserLocation(models.Model):
    user = models.ForeignKey(User, related_name='user_locations_id', on_delete=models.CASCADE)
    user_locations = models.PointField(geography=True, default=Point(0.0, 0.0))
    status = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s"%(self.user, self.user_locations)

    def save(self, *args, **kwargs):
        if self.status == True:
            UserLocation.objects.filter(user = self.user, status=True).update(status=False)
            self.status = True
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "User Location"
