from rest_framework import generics
from .models import Image
from .serializers import ImageSerializer


class ListImage(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class DetailImage(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
