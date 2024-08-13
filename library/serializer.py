from datetime import timedelta, datetime

import pytz
from rest_framework import serializers

from config import settings
from library.models import Author, Book, LogService
from library.services import check_count_of_book
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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        books = validated_data.pop('book')
        users = validated_data.pop('user')

        if not check_count_of_book(books):
            raise serializers.ValidationError('Книги закончились')

        log = LogService.objects.create(**validated_data)
        log.date_when_the_book_was_returned = datetime.now(pytz.timezone(settings.TIME_ZONE)) + timedelta(days=30)
        log.save()

        log.book.set(book.id for book in books)
        log.user.set([user.id for user in users])

        for book in books:
            book_instance = Book.objects.get(id=book.id)
            book_instance.count -= 1
            book_instance.save()

        return log

    def update(self, instance, validated_data):
        books_to_return = validated_data.get('book', [])
        if not books_to_return:
            raise serializers.ValidationError('Не указаны книги для возврата')

        for book in books_to_return:
            if book in instance.book.all():
                book_instance = Book.objects.get(id=book.id)
                book_instance.count += 1
                book_instance.save()
                instance.book.remove(book_instance)

        if instance.book.count() == 0:
            instance.book_on_user = False

        instance.book_return_date = datetime.now(pytz.timezone(settings.TIME_ZONE))
        instance.save()
        return instance

    class Meta:
        model = LogService
        fields = ['book', ]
