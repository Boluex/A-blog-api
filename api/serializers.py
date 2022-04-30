from.models import post,comment
from rest_framework.serializers import SerializerMethodField,HyperlinkedModelSerializer,ModelSerializer
from rest_framework import serializers

class homeserializer(ModelSerializer):
    author=SerializerMethodField('get_author')
    class Meta:
        model = post
        fields=['id','author','title','image','content','date_posted']

    def get_author(self,post):
        author=post.author.username
        return author



class createserializer(ModelSerializer):
    class Meta:
        model = post
        fields = [ 'title', 'image', 'content', 'date_posted']


class commentserializer(ModelSerializer):
    author=SerializerMethodField('get_author')
    posts=SerializerMethodField('get_post')
    class meta:
        model=comment
        fields=['author','posts','image','title','date_posted']

    def get_author(self,comment):
        author = comment.author.username
        return author

    def get_post(self,comment):
        post=comment.posts
        return post


class create_comment(ModelSerializer):
    class Meta:
        model = comment
        fields = [  'image', 'content', 'date_posted']
