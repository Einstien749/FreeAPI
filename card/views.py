from django.shortcuts import render

from rest_framework import generics

from .models import *

from .serializers import *

# Create your views here.

class AfricaView(generics.ListAPIView):

    queryset = Africa.objects.all()

    serializer_class = AfricaSerializer


class HumanView(generics.ListCreateAPIView):

    queryset = Human.objects.all()

    serializer_class = HumanSerializer
