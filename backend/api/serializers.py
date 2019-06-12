from rest_framework import serializers
from .models import Image
from django.conf import settings

class ImageSerializer(serializers.ModelSerializer):
    path_to_img = serializers.SerializerMethodField()

    def get_path_to_img(self, obj):
        print(self.context)
        return self.context.get('request').build_absolute_uri(obj.img.url)

    class Meta:
        model = Image
        fields = ('date', 'place', 'path_to_img')
