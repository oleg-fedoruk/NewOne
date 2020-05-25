from django.urls import path
from . import views

urlpatterns = [
    path('', views.RedListView.as_view(), name='home'),
    path('post/<int:pk>/', views.RedDetailView.as_view(), name='post_detail'),
    path('post/new/', views.RedCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.RedUpdateView.as_view(), name='post_edit'),

    ]
