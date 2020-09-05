from django.db import models

class Car(models.Model):  
    transmission_variants = [
        (0, 'manual'),
        (1, 'automatic'),
        (2, 'robot')
    ]
    producer = models.CharField(max_length=15)  
    model = models.CharField(max_length=5)  
    prod_year = models.IntegerField()
    transmission = models.SmallIntegerField(choices=transmission_variants, default=0)
    color = models.TextField()
    def __str__(self):
        return self.producer


