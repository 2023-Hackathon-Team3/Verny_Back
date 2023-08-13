from rest_framework import serializers
from .models import *
from django.db.models import Q
from rest_framework.serializers import ReadOnlyField


class RecommentSerializer(serializers.ModelSerializer):
    relikes_count = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Recomment
        fields = (
            "id",
            "author",
            "author_username",
            "created_at",
            "content",
            "relikes",
            "relikes_count",
        )
    read_only_fields = ["author"]
    def get_relikes_count(self, obj):
        return obj.relikes.count()
    
    def get_author_username(self, obj):
        return obj.author.username

class CommentSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    recomments_count = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "author_username",
            "content",
            "created_at",
            "likes",
            "likes_count",
            #"recomments",
            "recomments_count",
        ]
    read_only_fields = ["author"]
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_recomments_count(self, obj):
        return obj.recomments.count()
    
    def get_author_username(self, obj):
        return obj.author.username

class CommentDetailSerializer(serializers.ModelSerializer):
    #comment_like = LikeSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    recomments = RecommentSerializer(many=True, read_only=True)
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "author_username",
            "post",
            "author",
            "content",
            "created_at",
            "likes",
            "likes_count",
            "recomments",
            #"recomment_count",
        ]
    read_only_fields = ["author"]
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_author_username(self, obj):
        return obj.author.username


class PostSerializer(serializers.ModelSerializer):
    #comment = CommentSerializer(many=True, read_only=True)
    scraps_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField() 
    image = serializers.ImageField(use_url=True)
    author_username = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [ 
            "id",
            "author",
            "author_username",
            "image",
            "description",
            "title",
            "painter",
            "type",
            "scraps_count",
            "comment_count",
            #"recomments_count"

        ]

        read_only_fields = ["author"]
    def get_scraps_count(self, obj):
        return obj.scraps.count()

    def get_comment_count(self, obj):
        return obj.comment.count() 
    
    def get_author_username(self, obj):
        return obj.author.username
    
class PostDetailSerializer(serializers.ModelSerializer):
    scraps_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [ 
            "id",
            "author",
            "author_username",
            "image",
            "description",
            "content",
            "title",
            "painter",
            "drawing_technique",
            "work_year",
            #"type_choices",
            "type",
            "scraps",
            "scraps_count",
            "created_at",
            #"comment",
            "comment_count",
        ]

        read_only_fields = ["author"]
    def get_scraps_count(self, obj):
        return obj.scraps.count()
    
    def get_comment_count(self, obj):
        return obj.comment.count() 
    
    def get_author_username(self, obj):
        return obj.author.username