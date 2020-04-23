# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.BoxOfficeViewSet, basename="boxOffice")

urlpatterns = [
    path('', include(router.urls), name='boxOffice'),
    path('root/', include(views.api_root), name='apiRoot'),
    path('boxOffice/<int:pk>/highlight/', views.BoxOfficeHighlight.as_view()),
]
