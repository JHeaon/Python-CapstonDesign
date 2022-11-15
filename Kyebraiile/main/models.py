from django.db import models

# Create your models here.


class BraiilePicture(models.Model):
    image = models.ImageField(default='media/default_img.jpeg')
