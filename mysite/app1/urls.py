from rest_framework import routers
from .views import MessageViewSet,messageNotRead
from django.urls import path, include

router=routers.DefaultRouter()
router.register("",MessageViewSet)


urlpatterns = [
    path('all/',include(router.urls) ),
    path('notread/',messageNotRead.as_view())
    
]