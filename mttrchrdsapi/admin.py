from django.contrib import admin
from .models import Show, ShowCategory, ShowCreator

admin.site.register(Show)
admin.site.register(ShowCreator)
admin.site.register(ShowCategory)