from django.db import models


class user(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
def __str__(self):
    return f"{self.username} ({self.email})"

class AdminUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.username} ({self.email})"
# Create your models here.

# Create your models here.
