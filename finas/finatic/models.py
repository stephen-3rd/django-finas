from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0, "Drafts"),
    (1, "Publish")
)


class Lust(models.Model):
    picture = models.ImageField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE())