from rest_framework import routers
from .views import MessageViewSet
from django.urls import path 

router=routers.DefaultRouter()
router.register("",MessageViewSet)

urlpatterns = [
    path('',router.urls ),
]