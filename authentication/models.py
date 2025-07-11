from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(10)])
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
    class Meta:
        ordering = ['-created_at']
    