from django.db import models

# Create your models here.
class Image(models.Model):
  name = models.CharField(max_length=40)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.name)

  class Meta:
        ordering = ['created']