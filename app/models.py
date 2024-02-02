from django.db import models
from django.contrib.auth.models import User

class Track(models.Model):
    performer = models.CharField(max_length=112, verbose_name="Исполнитель")
    coperformer = models.CharField(max_length=112, verbose_name="Соисполнитель", null=True, blank=True)
    song = models.CharField(max_length=112, verbose_name="Песня")
    year = models.IntegerField(verbose_name="Год")
    image = models.ImageField(verbose_name="Фото", upload_to='images', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")


    def __str__(self):
        return self.title
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.track.song
    