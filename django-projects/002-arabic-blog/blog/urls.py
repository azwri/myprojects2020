from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    # path('detail/<int:post_id>/', views.detail, name='detail'),
    path('detail/<str:title>/', views.detail, name='detail'),
]
