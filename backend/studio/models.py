from django.db import models


class Studio(models.Model):
  name = models.CharField(max_length=300 , null=True)
  logo = models.CharField(max_length=1000 , null=True)
  description = models.TextField(null=True)
  established_date = models.DateField(auto_now_add=False)

  def __str__(self):
    return self.name