
import django_filters

from .serializers import (
    GenreSerializer,
    CardSerializer,
    CommentSerializer
)

from .models import *

from rest_framework.viewsets import ModelViewSet

from rest_framework.pagination import PageNumberPagination

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import filters

class GenreAPIView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']




class GenreRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination






class CardModelViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    pagination_class = PageNumberPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']




class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
