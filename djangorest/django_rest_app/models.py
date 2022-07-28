from django.db import models

Availability_choice = (
    ("BORROWED", "BORROWED"),
    ("AVAILABLE", "AVAILABLE"),
)


# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available = models.CharField(choices=Availability_choice, default="AVAILABLE", max_length=100)
    publisher = models.CharField(max_length=100)

    def __str___(self):
        return self.name


class Members(models.Model):
    Member_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

    def __str___(self):
        return self.username
