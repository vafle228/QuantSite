from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import ChangeUser, ChangeUserImg
from django.views.generic import ListView
from .models import News, Achievements


class showNewsProfile(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = News
    template_name = 'adminsAPI/profile/profilepage(news).html'
    context_object_name = 'all_news'
    ordering = ['-date']


class showAchievementProfile(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = Achievements
    template_name = 'adminsAPI/profile/profilepage(achievement).html'
    context_object_name = 'all_achievements'
    ordering = ['-date']


def changeUser(request):
    if request.method == 'POST':
        img_profile = ChangeUserImg(request.POST, request.FILES, instance=request.user.admins)
        update_user = ChangeUser(request.POST, instance=request.user)

        if img_profile.is_valid() and update_user.is_valid():
            img_profile.save()
            update_user.save()

            return redirect('/main/admins/profile/news')
    else:
        img_profile = ChangeUserImg(request.POST, request.FILES, instance=request.user.admins)
        update_user = ChangeUser()

    data = {
        'img_profile': img_profile,
        'update_user': update_user,
    }

    return render(request, 'adminsAPI/profile/change.html', data)


class CreateNews(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'tag', 'description', 'short_description', 'news_img']
    template_name = 'adminsAPI/news/create.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class UpdateNews(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title', 'tag', 'description', 'short_description', 'news_img']
    template_name = 'adminsAPI/news/update.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True
        return False


class DeleteNews(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/main/'
    template_name = 'main/delete.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True
        return False


class CreateAchievements(LoginRequiredMixin, CreateView):
    model = Achievements
    fields = ['achievement_img']
    template_name = 'adminsAPI/achievement/create.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class UpdateAchievements(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Achievements
    fields = ['achievement_img']
    template_name = 'adminsAPI/achievement/update.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        achievement = self.get_object()
        if self.request.user == achievement.autor:
            return True
        return False


class DeleteAchievements(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Achievements
    success_url = '/main/'
    template_name = 'main/delete.html'

    def test_func(self):
        achievement = self.get_object()
        if self.request.user == achievement.autor:
            return True
        return False
