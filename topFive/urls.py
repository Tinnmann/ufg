from django.urls import path
from topFive import views

urlpatterns = [
    path('', views.novelSeriesIndex, name='novelSeriesIndex'),
    path('<int:pk>/', views.novelSeriesDetail, name='novelSeriesDetail'),
    path("blog/", include("blog.urls")),
]
