from django.contrib import admin
from django.urls import path
from tweets.views import home_view, tweet_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('<int:tweet_id>', tweet_detail_view)
]
