from rest_framework import serializers

from library.models import Author, Book
from users.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        model = Book
        fields = '__all__'


class LogServiceSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Book
        fields = '__all__'
