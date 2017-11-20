from django.db import models

# Create your models here.

class Profile(models.Model):
    Username = models.CharField(max_length=200)
    email =models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
   # profilepic_url = models.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.Username

