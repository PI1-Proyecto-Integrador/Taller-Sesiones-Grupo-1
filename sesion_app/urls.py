from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_a, name='principal.html'),
    path('page_a/', views.page_a, name='page_a'),
    path('page_b/', views.page_b, name='page_b'),
    path('page_c/', views.page_c, name='page_c'),
    path('resume/', views.summary, name='resume'),
]
