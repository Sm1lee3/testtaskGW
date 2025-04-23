from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Menu
from api.serializers import MenuSerializer 
from .forms import MenuForm
import requests
#Головна сторінка
def index(request):
    # response = requests.get('http://127.0.0.1:8000/api/parent')
    # itemsapi = response.json()
    items = Menu.objects.filter(parent=None)

    serializer = MenuSerializer(items, many=True)
    itemsapi = serializer.data
    return render(request, 'menu/alllists.html', {'items': items,
        'itemsapi': itemsapi,})  

#Створення пунктів меню
def createmenu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MenuForm()
    return render(request, 'menu/createmenu.html', {'form': form})
#Редагування пунктів меню
def updatemenu(request, pk):
    menu_item = get_object_or_404(Menu, pk=pk)

    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = MenuForm(instance=menu_item)

    return render(request, 'menu/editmenu.html', {'form': form})
#Видалення пунктів меню
def delete(request, pk):
    menu_item = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        menu_item.delete()
        return redirect('index')
    return render(request, 'menu/deletemenu.html', {'menu_item': menu_item})



#Кастомна обробка помилок
def custom_500(request):
    # if request.path.startswith('/api/'):
    if '/api/' in request.path:
        return JsonResponse({'status': 500, 'message': 'Opps, server problems'}, status=500)
    return render(request, '500err.html', status=500)

def custom_404(request, exception):
    if '/api/' in request.path:
        return JsonResponse({'status': 404, 'message': 'Resource not found'}, status=404)
    return render(request, '404err.html', status=404)

#Повернення кастомної помилки 500
def error5(request): raise Exception('This is a test error')