from rest_framework import serializers
from .models import Post, Careers


class PostSerliazer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Post


class CareersSerliazer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Careers
