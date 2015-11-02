from courts.models import Court
from courts.serializers import CourtSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CourtList(APIView):
    """
    List all courts, or create a new court
    """
    def get(self, request, format=None):
        courts = Court.objects.all()
        serializer = CourtSerializer(courts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourtDetail(APIView):
    """
    Retrieve, update or delete a court instance
    """
    def get_object(self, id):
        try:
            return Court.objects.get(id=id)
        except Court.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        court = self.get_object(id)
        serializer = CourtSerializer(court)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        court = self.get_object(id)
        serializer = CourtSerializer(court, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        court = self.get_object(id)
        court.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
