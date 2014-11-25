from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.CharField(max_length=1024)
    
    def __unicode__(self):
        return '{} ({})'.format(self.name, self.description)

    
class ProductPicture(models.Model):
    path =  models.ImageField()
    product = models.ForeignKey('Product')