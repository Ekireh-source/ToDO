from pyexpat import model
from rest_framework import serializers
from .models import Post
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = User
        fields = ['id', 'email', 'todo', 'owner']



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'item', 'created']

