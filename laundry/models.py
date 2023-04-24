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

    STATUS = (
        ('Pending','pending'),
        ('Completed','completed')
    )
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
    status = models.CharField(default='Pending',max_length=15, choices=STATUS)

    def __str__(self):
        return str(self.std_id)
    
    @property
    def get_total(self):
        total = self.Kurta+self.Pajama+self.Shirt+self.T_Shirt+self.Pant+self.Lower+self.Shorts+self.Bedsheet+self.Pillow_Cover+self.Towel+self.Dupatta
        return total
    




class query(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Laundry_id = models.IntegerField()
    Problem = models.TextField(max_length=200)

    def __str__(self):
        return str(self.cloth_id)