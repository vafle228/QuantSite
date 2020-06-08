from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

tags = (
    ('vr/ar', '#VR/AR'),
    ('robots', '#Robots'),
    ('energy', '#Energy'),
    ('it', '#IT'),
    ('design', '#Design'),
    ('hitech', '#HiTech')
)


class News(models.Model):
    tag = models.CharField(max_length=60, choices=tags)
    title = models.CharField(max_length=60)
    description = models.TextField()
    short_description = models.CharField(max_length=150)
    date = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    news_img = models.ImageField(upload_to='news_img', default='news.png')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})

    def save(self, width=None, *args, **kwargs):
        super(News, self).save(*args, **kwargs)

        image = Image.open(self.news_img.path)
        w, h = image.size
        height = 800

        if width and height:
            max_size = (width, height)
        elif width:
            max_size = (width, h)
        elif height:
            max_size = (w, height)

        image.thumbnail(max_size, resample=Image.ANTIALIAS)
        image.save(self.news_img.path)


class Achievements(models.Model):
    date = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement_img = models.ImageField(upload_to='achievements_img', default='achievement')

    @staticmethod
    def get_absolute_url():
        return reverse('achievements_profile')

    def save(self, *args, **kwargs):
        super(Achievements, self).save(*args, **kwargs)

        image = Image.open(self.achievement_img.path)
        w, h = image.size
        if w > h:
            width = 1080
            height = None
        elif w == h:
            width = 600
            height = 600
        else:
            height = 800
            width = None

        if width and height:
            max_size = (width, height)
        elif width:
            max_size = (width, h)
        elif height:
            max_size = (w, height)

        image.thumbnail(max_size, resample=Image.ANTIALIAS)
        image.save(self.achievement_img.path)
