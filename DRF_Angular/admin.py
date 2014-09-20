from django.contrib import admin

from .models import Obj, ObjCategory, ObjProperty, ObjImage
# Register your models here.


class ObjPropertyInline(admin.StackedInline):
    model = ObjProperty
    fk_name = 'obj'
    extra = 1


class ObjCategoryInline(admin.StackedInline):
    model = ObjCategory.obj.through
    fk_name = 'obj'
    extra = 1


class ObjImageInline(admin.StackedInline):
    model = ObjImage
    fk_name = 'obj'
    extra = 1


class ObjInline(admin.StackedInline):
    model = Obj
    fk_name = 'obj'
    extra = 1


class ObjAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [
        ObjPropertyInline,
        ObjCategoryInline,
        ObjImageInline,
    ]


class ObjCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)


class ObjPropertyAdmin(admin.ModelAdmin):
    list_display = ('prop', 'obj')


class ObjImageAdmin(admin.ModelAdmin):
    list_display = ('filename', 'obj')


admin.site.register(Obj, ObjAdmin)
admin.site.register(ObjProperty, ObjPropertyAdmin)
admin.site.register(ObjCategory, ObjCategoryAdmin)
admin.site.register(ObjImage, ObjImageAdmin)
