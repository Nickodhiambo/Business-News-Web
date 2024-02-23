from django.urls import path
from . import views

app_name = 'news_content'


urlpatterns = [
        #Index
        path('index/', views.ContentView.as_view(), name='index'),

        # About
        path('about/', views.about_us, name='about')
        ]
