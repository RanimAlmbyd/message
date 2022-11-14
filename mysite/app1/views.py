
# Create your views here.
from django.http.response import JsonResponse
from rest_framework import viewsets

from .models import Message
from .serializer import MessageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    


class messageNotRead(APIView):
    def get(self,request) :
        mess=Message.objects.filter(read=False)
        s1=MessageSerializer(mess,many=True)
        return Response(s1.data)   