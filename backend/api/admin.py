from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings
from .models import Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
     def image(self, obj):
        print(obj)
        return format_html('<img src="%s"/>' % (settings.BASE_URL + obj.img.url))
     # admin_image.allow_tags = True
     list_display = ('img', 'image')
admin.site.register(Image, ImageAdmin)
