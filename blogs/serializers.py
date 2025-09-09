from rest_framework import serializers
from .models import Blog,Comment


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'


class BlogSerializers(serializers.ModelSerializer):
    comments= CommentSerializers(many=True, read_only=True) #related name should be the variable from model (related_name='comments')
    class Meta:
        model=Blog
        fields='__all__'        