# from django.shortcuts import render
from .models import Post, Careers
from .serializer import PostSerliazer, CareersSerliazer
from rest_framework import generics

# Create your views here.


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerliazer


class PostDetail(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerliazer


class CareersList(generics.ListAPIView):
    queryset = Careers.objects.all()
    serializer_class = CareersSerliazer


class CareersDetail(generics.ListAPIView):
    queryset = Careers.objects.all()
    serializer_class = CareersSerliazer
