from django.urls import path
from .views import *

urlpatterns = [
    path('profile/news', showNewsProfile.as_view(), name='news_profile'),
    path('profile/achievements', showAchievementProfile.as_view(), name='achievements_profile'),
    path('profile/user/change', changeUser),
    path('news/create/', CreateNews.as_view()),
    path('news/<int:pk>/update', UpdateNews.as_view(), name='update_news'),
    path('news/<int:pk>/delete/', DeleteNews.as_view(), name='news_delete'),
    path('achievement/create/', CreateAchievements.as_view()),
    path('achievement/<int:pk>/update', UpdateAchievements.as_view(), name='update_achievement'),
    path('achievement/<int:pk>/delete/', DeleteAchievements.as_view(), name='achievement_delete'),
]

