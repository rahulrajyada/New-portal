from django.contrib.auth.models import Group, User
from rest_framework import serializers
from newspaper.models import  Post


class UserSerializer(serializers.ModelSerializer): # HyperlinkedModelSerializer yo default ma use hun thiyo sikhau na ko lagi but real time ma hamile ModelSerializer use garxam
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'first_name', 'last_name']  # yaha hamile url ko satta id garxam kina ki url ko khasai kam hudaina


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
        
        
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "featured_image",
            "status",
            "tag",
            "category",
            #read only  / yo haru chai paila dekhi hudaina yo haru chai read garna lagi matrai ho
            "author",
            "views_count",
            "published_at",
        ]
        # yo read only garauna lagi hami le yo extra_kwargs use garxam
        extra_kwargs = {
            "author": {"read_only": True},
            "views_count": {"read_only": True },
            "published_at": {"read_only": True},
        }
        
    #jo login user tiyo
    def validate(self, data):
       data["author"] = self.context["request"].user
       return data