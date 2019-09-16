from django.urls import path
from topFive import views

urlpatterns = [
    path('', views.novelSeriesHome, name='novelSeriesHome'),
    path('', views.novelSeriesIndex, name='novelSeriesIndex'),
    path('<int:pk>/', views.novelSeriesDetail, name='novelSeriesDetail'),
]
