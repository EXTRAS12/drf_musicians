from django.db import models


class Musician(models.Model):
    """Исполнитель"""
    name = models.CharField(max_length=50)


class Album(models.Model):
    """Модель альбома"""
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE,
                                 related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)


class Track(models.Model):
    """Модель песня"""
    title = models.CharField(max_length=100)
    serial_number = models.ManyToManyField(Album, through="TrackLink")


class TrackLink(models.Model):
    """Промежуточная модель для добавления трека в альбом и порядковый номер"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name="Альбом")
    track = models.ForeignKey(Track, on_delete=models.CASCADE, verbose_name="Песня")
    number = models.IntegerField(verbose_name="Порядковый номер")