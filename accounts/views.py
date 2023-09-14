from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

from .utils import send_greeting


from .models import Greeting
from .serializers import GreetingSerializer


class GreetingViewSet(ModelViewSet):
    model = Greeting
    serializer_class = GreetingSerializer
    queryset = Greeting.objects.all()
    permission_classes = [TokenHasReadWriteScope]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if request.data["message"] == "hello":
            send_greeting("goodbye")
        return Response(data=serializer.data, status=HTTP_200_OK)
