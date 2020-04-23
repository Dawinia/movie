from django.http import HttpResponse, JsonResponse
from .serializers import BoxOfficeSerializer, MovieInfoSerializer
from .models import BoxOffice, MovieInfo
from rest_framework import generics, renderers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.

def index(request):
    return HttpResponse("hello, world!")


class BoxOfficeViewSet(viewsets.ReadOnlyModelViewSet, generics.ListAPIView):
    """
    BoxOffice viewset
    provides list and detail actions
    """
    queryset = BoxOffice.objects.all()
    serializer_class = BoxOfficeSerializer


class MovieInfoViewSet(viewsets.ReadOnlyModelViewSet, generics.ListAPIView):
    """
    MovieInfo viewset
    """
    queryset = MovieInfo.objects.all()
    serializer_class = MovieInfoSerializer
