from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-first-page'),
    path('about/', views.about, name='about-second-page'),
    path('third/', views.third, name='third-page'),
]
