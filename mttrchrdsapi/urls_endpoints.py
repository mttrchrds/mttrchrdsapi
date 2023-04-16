from django.urls import path
from mttrchrdsapi import views

urlpatterns_endpoints = [
    path('shows/', views.show_list),
    path('shows/<int:id>', views.show_detail),
    path('show-creators/', views.show_creator_list),
    path('show-creators/<int:id>', views.show_creator_detail),
    path('show-platforms/', views.show_platform_list),
    path('show-platforms/<int:id>', views.show_platform_detail),
    path('show-categories/', views.show_category_list),
    path('show-categories/<int:id>', views.show_category_detail),
    path('games/', views.game_list),
    path('games/<int:id>', views.game_detail),
    path('game-creators/', views.game_creator_list),
    path('game-creators/<int:id>', views.game_creator_detail),
    path('game-platforms/', views.game_platform_list),
    path('game-platforms/<int:id>', views.game_platform_detail),
    path('game-categories/', views.game_category_list),
    path('game-categories/<int:id>', views.game_category_detail),
]
