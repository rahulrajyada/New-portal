from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from api.serializers import GroupSerializer, PostSerializer, UserSerializer
from newspaper.models import Post

# yo frame work use gare paxi viewsets ma CURD  operation inbuild aai halxa

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined') # this is for filter ani order_by le chai latest joined lai mathi rakhdinxa 
    serializer_class = UserSerializer # yo create ra update garne bela use hunxa
    permission_classes = [permissions.IsAdminUser] # yo chai permission haru ko lagi use hunxa / default ma IsAuthenticated hunxa tara hami le IsAdminUser banau nu parxa


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
    

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Posts to be viewed or edited.
    """
    
    queryset = Post.objects.all().order_by("-published_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]  # yo permission haru chai admin le matrai dina pauxa
    
    def get_queryset(self):
        queryset = (
            super().get_queryset()# mathi ko queryset call gareko
            )
        if self.action in ["list", "retrieve"]: # filter use gareko
            queryset = queryset.filter(status="active", published_at__isnull=False)
        return queryset
    
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()