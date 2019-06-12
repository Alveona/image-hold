from rest_framework import routers
from django.urls import path
from .views import ImageView, ImagesView

router = routers.DefaultRouter(trailing_slash=True)
# router.register(r'photo', ImageView, base_name='photo')
urlpatterns = router.urls
urlpatterns += path('photo', ImageView.as_view()),
urlpatterns += path('photos', ImagesView.as_view()),
