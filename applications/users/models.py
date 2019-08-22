from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # This is left here to show the default fields
    # that can be enabled in the serializer
    # username = models.CharField()
    # first_name = models.CharField(blank=True)
    # last_name = models.CharField(blank=True)
    # email = models.EmailField(blank=True)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True,)
    # date_joined = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.id} - {self.username} Admin:{self.is_staff} Active:{self.is_active}'
