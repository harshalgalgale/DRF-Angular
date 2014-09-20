from django.conf.urls import url, include, patterns, static

from django.contrib import admin

from rest_framework import routers

from .views import ObjViewSet, CategoryViewSet, PropertyViewSet, ImageViewSet

admin.autodiscover()

# automatic URL routing.

router = routers.DefaultRouter()
router.register(r'objects', ObjViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'images', ImageViewSet)

# Additionally, we include login URLs for the browseable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
