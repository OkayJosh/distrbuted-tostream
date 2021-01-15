from django.db import models

class PriceIndex(models.Model):
    CHOICES = (
        ['Maize', 'MZ'], 
        ['Cocoa', 'CO'],
        ['Soyabeans', 'SO'],
        ['Paddy_Rice', 'Ri'],
        ['Sorghum', 'SG'], 
        ['Ginger', 'Gi']
    )
    name = models.CharField(max_length=12, choices=CHOICES, default="Maize")
    price = models.FloatField(default=170.55)