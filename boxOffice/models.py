from django.db import models


# Create your models here.
class MovieInfo(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    dbMovieID = models.IntegerField(db_column='dbMovieID')
    tppMovieID = models.IntegerField(db_column='tppMovieID')
    movieName = models.CharField(max_length=32, db_column='movieName')
    directors = models.CharField(max_length=64, db_column='directors')
    writers = models.CharField(max_length=128, db_column='writers')
    actors = models.CharField(max_length=256, db_column='actors')
    genre = models.CharField(max_length=32, db_column='genre')
    area = models.CharField(max_length=32, db_column='area')
    rateCount = models.IntegerField(db_column='rateCount')
    doubanRate = models.FloatField(db_column='doubanRate')
    duration = models.SmallIntegerField(db_column='duration')
    publishedDate = models.DateField(db_column='publishedDate')

    class Meta:
        db_table = 'movieInfo'


class BoxOffice(models.Model):
    # movieInfo = models.ForeignKey('MovieInfo', on_delete=models.CASCADE, related_name='movie_boxOffice',
    #                               db_column='tppMovieID', to_field='dbMovieID') TODO: 外键
    id = models.IntegerField(primary_key=True, db_column='id')
    movieId = models.IntegerField(db_column='movieID')
    movieName = models.CharField(max_length=32, db_column='movieName')
    seatRate = models.CharField(max_length=5, db_column='seatRate')
    boxInfo = models.FloatField(db_column='boxInfo')
    boxRate = models.CharField(max_length=5, db_column='boxRate')
    releaseInfo = models.CharField(max_length=10, db_column='releaseInfo')
    showInfo = models.IntegerField(db_column='showInfo')
    showRate = models.CharField(max_length=5, db_column='showRate')
    splitBoxInfo = models.FloatField(db_column='splitBoxInfo')
    splitSumBoxInfo = models.FloatField(db_column='splitSumBoxInfo')
    sumBoxInfo = models.FloatField(db_column='sumBoxInfo')
    showView = models.SmallIntegerField(db_column='showView')
    crawlDate = models.DateField(db_column='crawlDate')
    yearRate = models.CharField(max_length=13, db_column='yearRate')

    class Meta:
        db_table = 'boxOffice'

