from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Admins(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='admins_img', default='admin.jpg')

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super(Admins, self).save(*args, **kwargs)

        image = Image.open(self.img.path)
        w, h = image.size
        if w > h:
            width = 1024
            height = None
        elif w == h:
            width = 512
            height = 512
        else:
            height = 512
            width = None

        if width and height:
            max_size = (width, height)
        elif width:
            max_size = (width, h)
        elif height:
            max_size = (w, height)

        image.thumbnail(max_size, resample=Image.ANTIALIAS)
        image.save(self.img.path)
