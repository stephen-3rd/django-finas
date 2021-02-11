from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0, "Drafts"),
    (1, "Publish")
)


class Lust(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    picture = models.ImageField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-date']
        # Class Meta was created so as to sort post by date in descending Order(Latest will appear first)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:10] + '  [...]'


