# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movieInfo', views.MovieInfoViewSet)
router.register(r'boxOffice', views.BoxOfficeViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    # path('', views.BoxOfficeViewSet.as_view({'get'})),
    # path('root/', include(views.api_root), name='apiRoot'),
    # path('boxOffice/<int:pk>/highlight/', views.BoxOfficeHighlight.as_view()),
]
