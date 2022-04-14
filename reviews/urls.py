from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.ReviewsList.as_view()),
    path('<int:pk>/', views.ReviewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)