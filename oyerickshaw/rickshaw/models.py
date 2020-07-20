from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()
class DriverRickshaw(models.Model):
    user = models.ForeignKey(User, related_name='user_rickshaw', on_delete=models.CASCADE)
    rickshaw_number = models.CharField(max_length=255, null = True)
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.status == True:
            DriverRickshaw.objects.filter(user = self.user, status=True).update(status=False)
            self.status = True
        super().save(*args, **kwargs)
