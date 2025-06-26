from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categori(models.Model):
    name = models.CharField(max_length = 65)

    def __str__(self):
        return self.name

class game(models.Model):
    title = models.CharField(max_length = 65)
    description = models.CharField(max_length = 165)
    slug = models.SlugField()
    end_game = models.CharField(max_length = 5)
    classification = models.CharField(max_length= 3)
    review_game = models.TextField()
    review_game_html = models.BooleanField(default= False)
    created_post = models.DateTimeField(auto_now_add=True)
    update_post = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='games/covers/%Y/%m/%d/')
    categori = models.ForeignKey(
        categori, on_delete = models.SET_NULL, null = True
    )
    def __str__(self):
        return self.title


    author = models.ForeignKey(
        User, on_delete = models.SET_NULL, null = True
    )