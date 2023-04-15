from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class ShowCreator(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shows/creators/', null=True, blank=True)

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
    

