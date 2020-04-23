# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import BoxOffice, MovieInfo


class BoxOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxOffice
        fields = (
            'movieId', 'movieName', 'seatRate', 'boxInfo', 'boxRate', 'releaseInfo', 'showInfo', 'showRate',
            'splitBoxInfo', 'splitSumBoxInfo', 'sumBoxInfo', 'showView', 'crawlDate', 'yearRate'
        )


class MovieInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = '__all__'
