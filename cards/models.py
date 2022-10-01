from django.db import models

class Card(models.Model):
    name=models.CharField(max_length=150)
    position = models.CharField(max_length=3)
    PAC = models.PositiveSmallIntegerField(null=True,blank=True)
    SHO = models.PositiveSmallIntegerField(null=True,blank=True)
    PAS = models.PositiveSmallIntegerField(null=True,blank=True)
    DRI = models.PositiveSmallIntegerField(null=True,blank=True)
    DEF = models.PositiveSmallIntegerField(null=True,blank=True)
    PHY = models.PositiveSmallIntegerField(null=True,blank=True)
    img = models.ImageField(null=True,blank=True)



    def __str__(self):
        return self.name