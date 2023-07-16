from rest_framework import serializers

from blog.models import Post, Comment
from blog.validators import ForbiddenWordsValidator


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = (
            'content',
            'author',
            'data_create',
            'data_update',
        )

    def create(self, validated_data):
        pk = self.context.get('request').path_info.split('/')[-4]
        post = Post.objects.filter(pk=pk).first()
        comment = Comment.objects.create(post=post, **validated_data)
        return comment


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='comment_set', many=True, required=False)
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'author',
            'image',
            'data_create',
            'data_update',
            'comments',
        )


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'image',
            'data_create',
            'data_update',
        )

        validators = [ForbiddenWordsValidator(field='title')]
