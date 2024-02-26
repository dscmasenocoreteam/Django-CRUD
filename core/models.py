from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    f_name = models.CharField(max_length=250)
    l_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    time_created = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f'{self.f_name} {self.l_name}'
