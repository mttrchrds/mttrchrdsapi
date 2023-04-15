from django.urls import path
from mttrchrdsapi import views

urlpatterns_endpoints = [
    path('shows/', views.show_list),
    path('shows/<int:id>', views.show_detail),
    path('show-creators/', views.show_creator_list),
]
