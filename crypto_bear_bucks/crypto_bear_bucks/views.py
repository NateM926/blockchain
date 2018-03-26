from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, CCWalletSerializer
from cc.models import Wallet, Currency

def index(request):
    return HttpResponse("Hello, world. You're at the openassets index.")

def generate_asset_id(request):
    return HttpResponse("do")

# Currenty the API lives in this single View / Serializer, eventually split into each app!

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CCWalletViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows wallet to be viewed or edited.
    """
    queryset = Wallet.objects.all()
    serializer_class = CCWalletSerializer
