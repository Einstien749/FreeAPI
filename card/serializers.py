from rest_framework import serializers

from .models import *

class AfricaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():

        model = Africa

        fields = ('id','country', 'capital')

class HumanSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():

        model = Human

        fields = ('id','name', 'sex', 'age')
