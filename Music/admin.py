from django.contrib import admin
from .models import Label, Genre, Band, Album, Track, Musician


class PrepopulateSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Label, PrepopulateSlugAdmin)
admin.site.register(Genre, PrepopulateSlugAdmin)
admin.site.register(Band, PrepopulateSlugAdmin)
admin.site.register(Album, PrepopulateSlugAdmin)
admin.site.register(Track, PrepopulateSlugAdmin)
admin.site.register(Musician)
