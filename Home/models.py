from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')  # Specify upload directory
    price = models.FloatField()
    def __str__(self):
        return self.name
