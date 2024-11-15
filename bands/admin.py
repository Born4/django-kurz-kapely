from django.contrib import admin
from bands import models

#admin.site.register(models.Band)
#admin.site.register(models.Album)
#admin.site.register(models.Song)
#admin.site.register(models.Artist)


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    # list_display = ('name')
    pass


@admin.register(models.Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'still_active', 'genre', 'get_full_name')

    @admin.display(description='Full name')
    def get_full_name(self, obj):
        return obj.full_name


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'band')


@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    #list_display = ('name', 'year')
    pass


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    #list_display = ('name', 'year')
    pass
