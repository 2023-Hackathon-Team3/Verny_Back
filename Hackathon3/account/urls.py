from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('mypage/', ProfileView.as_view()),
    #path('my_scraped_page/', MyScrapedPostsView.as_view()),
    #path('my_posted_page/', MyScrapedPostsView.as_view()),
    #path('my_comments_page/', MyScrapedPostsView.as_view()),
]