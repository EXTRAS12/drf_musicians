from django.urls import path

from .views import (AlbumViewSet, MusicianViewSet, TrackLinkViewSet,
                    TrackViewSet)

urlpatterns = [
    path('musicians/', MusicianViewSet.as_view({"get": "list", "post": "create"})),
    path('albums/', AlbumViewSet.as_view({"get": "list", "post": "create"})),
    path('tracks/', TrackViewSet.as_view({"get": "list", "post": "create"})),
    path('tracklinks/', TrackLinkViewSet.as_view({"get": "list", "post": "create"})),
]