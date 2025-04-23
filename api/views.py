from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from menu.models import Menu
from .serializers import MenuSerializer

@api_view(['GET'])
def getData(request):
    items = Menu.objects.all()
    serializer = MenuSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getParent(request):
    items = Menu.objects.filter(parent=None)
    serializer = MenuSerializer(items, many=True)
    return Response(serializer.data)

def error_404(request, exception):
    responce_data = {
        'status': 404,
        'message': 'Resourse not found, ',
    }
    return JsonResponse(responce_data, status=404)

def error_500(request, exception):
    responce_data = {
        'status': 500,
        'message': 'Opps, server problems ',
    }
    return JsonResponse(responce_data, status=500)
