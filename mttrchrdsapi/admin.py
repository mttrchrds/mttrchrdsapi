from django.contrib import admin
from .models import Show, ShowCategory, ShowCreator, ShowPlatform, Game, GameCategory, GameCreator, GamePlatform, Activity

admin.site.register(Show)
admin.site.register(ShowCreator)
admin.site.register(ShowCategory)
admin.site.register(ShowPlatform)
admin.site.register(Game)
admin.site.register(GameCreator)
admin.site.register(GameCategory)
admin.site.register(GamePlatform)
admin.site.register(Activity)