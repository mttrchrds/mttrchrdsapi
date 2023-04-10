from django.urls import path
from mttrchrdsapi import views

urlpatterns_api = [
    path('shows/', views.show_list),
    path('shows/<int:id>', views.show_detail),
]
