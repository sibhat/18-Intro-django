from django.db import models
from uuid import uuid4
# Create your models here.
class Graph(models.Model):
    # id= models.UUID()
    title= models.CharField(max_length=200)
    content=models.TextField(blank=True)

