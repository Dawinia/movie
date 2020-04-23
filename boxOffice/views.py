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


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'boxOffice': reverse('boxOffice-list', request=request, format=format),
        'movieInfo': reverse('movieInfo-list', request=request, format=format),
    })


class BoxOfficeViewSet(viewsets.ReadOnlyModelViewSet, generics.ListAPIView):
    queryset = BoxOffice.objects.all()
    serializer_class = BoxOfficeSerializer


class BoxOfficeHighlight(generics.GenericAPIView):
    queryset = BoxOffice.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        boxOffice = self.get_object()
        return Response(boxOffice.highlighted)


class MovieInfoViewSet(viewsets.ReadOnlyModelViewSet, generics.ListAPIView):
    queryset = MovieInfo.objects.all()
    serializer_class = MovieInfoSerializer
