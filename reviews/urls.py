from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_list),
    path('<int:pk>/', views.review_detail),
]