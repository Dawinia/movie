from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import BoxOfficeSerializers
from .models import BoxOffice
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers


# Create your views here.

def index(request):
    return HttpResponse("hello, world!")


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'boxOffice': reverse('boxOffice-list', request=request, format=format),
    })


class BoxOfficeViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = BoxOffice.objects.all()
    serializer_class = BoxOfficeSerializers


class BoxOfficeHighlight(generics.GenericAPIView):
    queryset = BoxOffice.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        boxOffice = self.get_object()
        return Response(boxOffice.highlighted)
