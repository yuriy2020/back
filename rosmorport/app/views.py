from app.models import App
from app.serializers import AppSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class AppList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        apps = App.objects.all()
        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppDetail(APIView):
    """
    Retrieve, update or delete a app instance.
    """
    def get_object(self, pk):
        try:
            return App.objects.get(pk=pk)
        except App.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        app = self.get_object(pk)
        serializer = AppSerializer(app)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        app = self.get_object(pk)
        serializer = AppSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        app = self.get_object(pk)
        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)