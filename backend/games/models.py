from django.db import models
from django.contrib.auth.models import User
from genre.models import Genre

class Game(models.Model):
  title = models.CharField(max_length=500 , null=True)
  short_description = models.TextField(null=True)
  description = models.TextField(null=True)
  genre_1 = models.ForeignKey(Genre , on_delete=models.CASCADE , null=True ,related_name="game_genre_1")
  genre_2 = models.ForeignKey(Genre , on_delete=models.CASCADE , null=True , related_name="game_genre_2")
  cover_photo = models.TextField(null=True)
  page_photo1 = models.TextField(null=True)
  page_photo2 = models.TextField(null=True)
  review_1 = models.IntegerField(null=True)
  review_2 = models.IntegerField(null=True)
  review_3  = models.IntegerField(null=True)
  review_4 = models.IntegerField(null=True)
  review_5 = models.IntegerField(null=True)
  master_review = models.IntegerField()
  price = models.DecimalField(decimal_places=2 , max_digits=10000 , null=True)
  published_date = models.DateField(auto_now_add=False , null=True)
  listed_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title