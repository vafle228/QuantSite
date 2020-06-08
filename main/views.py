from django.shortcuts import render
from adminsAPI.models import News, Achievements
from django.views.generic import ListView, DetailView


def showQuantSite(request):
    news = {
        'first_news': News.objects.all()[len(News.objects.all()) - 1],
        'second_news': News.objects.all()[len(News.objects.all()) - 2],
        'third_news': News.objects.all()[len(News.objects.all()) - 3]
    }
    return render(request, 'main/index.html', news)


def showTeachersSite(request):
    return render(request, 'main/teachers.html')


def showAboutSite(request):
    return render(request, 'main/about.html')


def showContactSite(request):
    return render(request, 'main/contact.html')


class NewsListView(ListView):
    model = News
    template_name = 'main/news/news.html'
    context_object_name = 'all_news'
    ordering = ['-date']
    paginate_by = 9


class NewsDetailView(DetailView):
    model = News
    template_name = 'main/news/detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        return ctx


class AchievementsListView(ListView):
    model = Achievements
    template_name = 'main/achievement/achievements.html'
    context_object_name = 'all_achievements'
    ordering = ['-date']
    paginate_by = 12
