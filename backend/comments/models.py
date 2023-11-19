from django.db import models
from games.models import Game
from django.contrib.auth.models import User

class Comment(models.Model):
  owner = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
  post = models.ForeignKey(Game , on_delete=models.CASCADE , null=True)
  commented_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.owner