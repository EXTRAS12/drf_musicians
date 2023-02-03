from django.contrib import admin

from .models import Album, Musician, Track

admin.site.register(Album)
admin.site.register(Musician)
admin.site.register(Track)
