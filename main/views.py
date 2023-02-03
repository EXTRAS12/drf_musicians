from rest_framework import viewsets
from rest_framework.response import Response

from .models import Album, Musician, Track, TrackLink
from .serializers import (AlbumSerializer, MusicianSerializer,
                          TrackLinkSerializer, TrackSerializer)


class MusicianViewSet(viewsets.ModelViewSet):
    """Получаем список музыкантов и возможность создать нового"""
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """Получаем список альбомов и возможность создать новый"""
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    """Получаем список песен и возможность создать новую"""
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackLinkViewSet(viewsets.ModelViewSet):
    """Добавляем песню в альбом и даём порядковый номер"""
    queryset = TrackLink.objects.all()
    serializer_class = TrackLinkSerializer