from .views import *
from django.urls import path, include
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', showQuantSite, name='main'),
    path('quants/', include('quants.urls')),
    path('admins/', include('adminsAPI.urls')),
    path('auth/', authViews.LoginView.as_view(template_name='main/log.html'), name='auth'),
    path('exit/', authViews.LogoutView.as_view(template_name='main/exit.html')),
    path('news/', NewsListView.as_view()),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('achievements/', AchievementsListView.as_view()),
    path('teachers/', showTeachersSite),
    path('about/', showAboutSite),
    path('contact/', showContactSite)
]
