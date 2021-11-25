from django.db import models
from django.contrib.auth.models import User
from django.forms.models import modelform_factory
from django.urls import reverse_lazy
# Create your models here.

STATUS = (
    (0, "Drafts"),
    (1, "Publish")
)


class Lust(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    picture = models.ImageField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Lust'
        # Class Meta was created so as to sort post by date in descending Order(Latest will appear first)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:10] + '  [...]'

class ReachMe(models.Model):
    name = models.CharField(max_length=300, blank=False)
    email = models.EmailField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name_plural = 'ReachMe' 