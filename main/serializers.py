from rest_framework import serializers

from .models import Album, Musician, Track, TrackLink


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ('id', 'name' )


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('title', )


class TrackLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackLink
        fields = ('album', 'track', 'number')

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'artist', 'created_at')