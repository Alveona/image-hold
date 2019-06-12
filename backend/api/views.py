from django.shortcuts import render
from .models import Image
from .serializers import ImageSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import dateutil.parser
from datetime import datetime

class ImageView(APIView):
    def post(self, request):
        img = request.FILES['img']
        place = request.data.get('place')
        size = img.size / 1024 # bytes --> kb
        obj = Image(img = img, place = place, size = size)
        obj.save()
        return Response(status = status.HTTP_200_OK)

class ImagesView(APIView):
    def get(self, request):
        date = self.request.query_params.get('date')
        size = self.request.query_params.get('size')
        parsed_date = dateutil.parser.parse(date)
        images = Image.objects.all().filter(date = parsed_date)
        for img in images:
            if int(img.size) > int(size):
                images = images.exclude(id = img.id)
        return Response(status = status.HTTP_200_OK, data = ImageSerializer(images, many=True, context={'request': request}).data)
