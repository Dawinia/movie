from django.contrib import admin
from .models import BoxOffice, MovieInfo


# Register your models here.

class BoxOfficeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['yearRate', 'crawlDate']}),
        ('movieInfo', {'fields': ['movieId', 'movieName', 'releaseInfo']}),
        ('boxOfficeInfo', {'fields': ['boxRate', 'boxInfo', 'splitBoxInfo', 'sumBoxInfo', 'splitSumBoxInfo']}),
        ('showInfo', {'fields': ['showInfo', 'showView', 'showRate', 'seatRate']})
    ]


admin.site.register(BoxOffice, BoxOfficeAdmin)
admin.site.register(MovieInfo)
