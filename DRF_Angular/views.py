from rest_framework import viewsets

from .models import Obj, ObjCategory, ObjProperty, ObjImage

from .serializers import ObjSerializer, ObjCategorySerializer, ObjPropertySerializer, ObjImageSerializer


class ObjViewSet(viewsets.ModelViewSet):
    queryset = Obj.objects.all()
    serializer_class = ObjSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ObjCategory.objects.all()
    serializer_class = ObjCategorySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = ObjProperty.objects.all()
    serializer_class = ObjPropertySerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ObjImage.objects.all()
    serializer_class = ObjImageSerializer

