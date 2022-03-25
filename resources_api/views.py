from rest_framework import generics
from .serializers import ResourceSerializer, ForumSerializer
from .models import Resource, Forum

# Create your views here.

class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all().order_by('id')
    serializer_class = ResourceSerializer

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all().order_by('id')
    serializer_class = ResourceSerializer

class ForumList(generics.ListCreateAPIView):
    queryset = Forum.objects.all().order_by('id')
    serializer_class = ForumSerializer

class ForumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forum.objects.all().order_by('id')
    serializer_class = ForumSerializer
