from django.contrib.auth.models import User, Group
from cc.models import Wallet, Currency
from rest_framework import serializers

# Currenty the API lives in this single View / Serializer, eventually split into each app!

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CCWalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wallet
        fields = ('balance', 'label')