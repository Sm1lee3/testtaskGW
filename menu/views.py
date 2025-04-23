from django.shortcuts import render
from django.http import JsonResponse
from .models import Menu
from api.serializers import MenuSerializer 
import requests
def index(request):
    # response = requests.get('http://127.0.0.1:8000/api/parent')
    # itemsapi = response.json()
    items = Menu.objects.filter(parent=None)

    serializer = MenuSerializer(items, many=True)
    itemsapi = serializer.data
    return render(request, 'menu/alllists.html', {'items': items,
        'itemsapi': itemsapi,})  

def custom_500(request):
    # if request.path.startswith('/api/'):
    if '/api/' in request.path:
        return JsonResponse({'status': 500, 'message': 'Opps, server problems'}, status=500)
    return render(request, '500err.html', status=500)

def custom_404(request, exception):
    if '/api/' in request.path:
        return JsonResponse({'status': 404, 'message': 'Resource not found'}, status=404)
    return render(request, '404err.html', status=404)


def error5(request): raise Exception('This is a test error')