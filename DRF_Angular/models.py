from django.db import models

from django.core.files import File

from DRF_Angular.settings import MEDIA_ROOT

import ntpath


class Obj(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class ObjCategory(models.Model):
    category = models.CharField(max_length=100)
    obj = models.ManyToManyField(Obj)

    def __str__(self):
        return self.category


class ObjProperty(models.Model):
    prop = models.CharField(max_length=100)
    obj = models.OneToOneField(Obj)

    def __str__(self):
        return self.prop


class ObjImage(models.Model):
    obj = models.ForeignKey(Obj)
    image = models.ImageField(upload_to=MEDIA_ROOT)
    filename = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.filename

    def save(self, *args, **kwargs):
        self.filename = ntpath.basename(self.image.url)
        super(ObjImage, self).save(*args, **kwargs)
