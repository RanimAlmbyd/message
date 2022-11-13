
from .serializer import MessageSerializer
from .models import Message
from rest_framework import viewsets
# Create your views here.


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        queryset = super(MessageViewSet, self).get_queryset()
        if self.request.GET.get('notification'):
            return queryset.filter(read=self.request.GET.get('notification'))
        return queryset