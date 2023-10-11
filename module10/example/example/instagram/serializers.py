from django.contrib.auth.models import User, Group
from rest_framework import serializers


from instagram.models import Post


class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Post
        fields = ['text', 'pub_date', 'image', 'id']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']