from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_assignment, name='submit'),
    path('list/', views.list_assignments, name='list'),
]
