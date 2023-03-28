#from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class clothe(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Student_id = models.CharField(max_length=30,primary_key=True)
    Kurta = models.IntegerField()
    Pajama = models.IntegerField()
    Shirt = models.IntegerField()
    T_Shirt = models.IntegerField()
    Pant = models.IntegerField()
    Lower = models.IntegerField()
    Shorts = models.IntegerField()
    Bedsheet = models.IntegerField()
    Pillow_Cover = models.IntegerField()
    Towel = models.IntegerField()
    Dupatta = models.IntegerField()
    std = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.std_id)
    

class clothes(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Kurta = models.IntegerField()
    Pajama = models.IntegerField()
    Shirt = models.IntegerField()
    T_Shirt = models.IntegerField()
    Pant = models.IntegerField()
    Lower = models.IntegerField()
    Shorts = models.IntegerField()
    Bedsheet = models.IntegerField()
    Pillow_Cover = models.IntegerField()
    Towel = models.IntegerField()
    Dupatta = models.IntegerField()
    std = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.std_id)
