from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
    Student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Student_id)

