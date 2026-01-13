from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    img_path = models.CharField(max_length=255)

    def __str__(self): # print(menu) 했을 때 name이 나오도록
        return self.name 