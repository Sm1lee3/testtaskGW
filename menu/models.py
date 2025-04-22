from django.db import models

# Create your models here
class Menu(models.Model):
    name = models.CharField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null = True, related_name='children')

    def __str__(self):
        return self.name