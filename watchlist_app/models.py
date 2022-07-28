from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name =models.CharField(max_length=50)
    movie_description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.movie_name