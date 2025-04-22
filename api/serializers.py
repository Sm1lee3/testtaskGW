from rest_framework import serializers
from menu.models import Menu

class MenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = '__all__'
# Рекурсивне отримання дочірніх елементів



    def get_children(self, obj):
        # Отримуємо дочірні елементи для поточного об'єкта
        children = Menu.objects.filter(parent=obj)
        return MenuSerializer(children, many=True).data