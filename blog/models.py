from django.db import models

from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from django.urls import reverse

from django.utils.text import slugify
from ckeditor.fields import RichTextField
import uuid
import datetime

# Create your models here.

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    """
    image upload directory setting
    e.g)
        images/{year}/{month}/{day}/{username}/{filename}
        images/2016/7/12/hjh/hjh-2016-07-12-158859.png
    """
    now = datetime.datetime.now()

    path = "images/{year}/{month}/{day}/{filename}".format(
        year=now.year,
        month=now.month,
        day=now.day,
        filename = "%s.%s" % (uuid.uuid4(), ext),
    )

    return path

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image_one = models.ImageField(upload_to=get_file_path, blank=True)
    image_two = models.ImageField(upload_to=get_file_path, blank=True)
    image_three = models.ImageField(upload_to=get_file_path, blank=True)
    image_four = models.ImageField(upload_to=get_file_path, blank=True)
    image_five = models.ImageField(upload_to=get_file_path, blank=True)
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    comments = GenericRelation(Comment)


    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return f"{self.title}"
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

