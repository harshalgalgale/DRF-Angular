from rest_framework import serializers

from .models import Obj, ObjCategory, ObjProperty, ObjImage


class ObjSerializer(serializers.ModelSerializer):

    class Meta:
        model = Obj
        fields = ('name', 'description')


class ObjCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ObjCategory
        fields = ('category', 'obj')


class ObjPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = ObjProperty
        fields = ('prop', 'obj')


class ObjImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ObjImage
        fields = ('obj', 'image', 'filename')
