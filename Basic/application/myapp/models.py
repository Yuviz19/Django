from django.db import models
from django.utils import timezone

class chaiVariety(models.Model):
    CHAI_CHOICE = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KI", "KIVI"),
        ("EL", "ELAICHI")        
    ]
    name = models.CharField(max_length=100)
    
    image = models.ImageField(upload_to="myapps/")
    
    date_added = models.DateTimeField(default=timezone.now)

    types = models.CharField(max_length=2,choices=CHAI_CHOICE)

    def __str__(self):
        return self.name