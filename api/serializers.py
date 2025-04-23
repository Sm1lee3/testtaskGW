from rest_framework import serializers
from menu.models import Menu
#Перетворення моделі в JSON
class MenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = '__all__'



    def get_children(self, obj):
        # Отримуємо дочірні елементи для поточного об'єкта
        children = Menu.objects.filter(parent=obj)
        return MenuSerializer(children, many=True).data