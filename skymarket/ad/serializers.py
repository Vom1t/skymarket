from phonenumber_field import serializerfields
from rest_framework import serializers

from ad.models import Ad, Comment


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'description')


class AdDetailSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='author.first_name')
    last_name = serializers.ReadOnlyField(source='author.last_name')
    phone = serializerfields.PhoneNumberField(source='author.phone', read_only=True)
    author_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Ad
        fields = ('pk', 'author_id', 'image', 'title', 'price', 'phone', 'first_name', 'last_name', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source='author.id')
    ad_id = serializers.ReadOnlyField(source='ad.id')
    first_name = serializers.ReadOnlyField(source='author.first_name')
    last_name = serializers.ReadOnlyField(source='author.last_name')

    class Meta:
        model = Comment
        fields = ('pk', 'text', 'created_at', 'author_id', 'ad_id', 'first_name', 'last_name')
