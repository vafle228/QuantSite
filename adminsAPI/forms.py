from django import forms
from django.contrib.auth.models import User
from main.models import Admins


class ChangeUser(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username']


class ChangeUserImg(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ChangeUserImg, self).__init__(*args, **kwards)
        self.fields['img'].label = "Изображение профиля"

    class Meta():
        model = Admins
        fields = ['img']
