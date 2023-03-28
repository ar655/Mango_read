from rest_framework import serializers

from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id username body post parent'.split()




class CardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Card
        fields = 'id name type year summary genre image genre_name comments'.split()

