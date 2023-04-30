from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)


    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8) 
    
    def get_discount(self):
        return "122"
    
    
