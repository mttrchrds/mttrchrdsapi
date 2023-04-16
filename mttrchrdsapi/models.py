from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class ShowCreator(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shows/creators/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class ShowPlatform(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shows/platforms/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class ShowCategory(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Show(BaseModel):
    name = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='shows/', null=True)
    creator = models.ForeignKey(
        ShowCreator,
        on_delete=models.SET_NULL,
        related_name='show',
        related_query_name='shows',
        null=True,
    )
    categories = models.ManyToManyField(
        ShowCategory,
        related_name='show',
        related_query_name='shows',
    )

    def __str__(self):
        return self.name
    

class GameCreator(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='games/creators/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class GamePlatform(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='games/platforms/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class GameCategory(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Game(BaseModel):
    name = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='games/', null=True)
    creator = models.ForeignKey(
        GameCreator,
        on_delete=models.SET_NULL,
        related_name='game',
        related_query_name='games',
        null=True,
    )
    categories = models.ManyToManyField(
        GameCategory,
        related_name='game',
        related_query_name='games',
    )

    def __str__(self):
        return self.name

class Activity(BaseModel):
    start_at = models.DateField(null=False, blank=False)
    end_at = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    show_activity = models.ForeignKey(
        Show,
        on_delete=models.SET_NULL,
        related_name='activity',
        related_query_name='activities',
        null=True,
        blank=True,
    )
    game_activity = models.ForeignKey(
        Game,
        on_delete=models.SET_NULL,
        related_name='activity',
        related_query_name='activities',
        null=True,
        blank=True,
    )
    show_platform = models.ForeignKey(
        ShowPlatform,
        on_delete=models.SET_NULL,
        related_name='activity',
        related_query_name='activities',
        null=True,
        blank=True,
    )
    game_platform = models.ForeignKey(
        GamePlatform,
        on_delete=models.SET_NULL,
        related_name='activity',
        related_query_name='activities',
        null=True,
        blank=True,
    )

    def __str__(self):
        name = ''
        if self.show_activity:
            name = self.show_activity.name
        if self.game_activity:
            name = self.game_activity.name
        platform = ''
        if self.show_activity:
            platform = self.show_platform.name
        if self.game_activity:
            platform = self.game_platform.name
        return str(self.start_at) + ' ' + name +  ' (' + platform + ')'

