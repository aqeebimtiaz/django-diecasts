from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class ProductTemplate(models.Model):
    parent_name = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length=200, unique = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    barcode = models.CharField(max_length=100, unique=True)
    manufacturer = models.CharField(max_length = 200)
    style = models.CharField(max_length=200)
    # type = models.ForeignKey()
    year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1960), max_value_current_year])
    link = models.CharField(max_length=200, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.parent_name

