from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    user_name=models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    class Meta:
        db_table:"user"
