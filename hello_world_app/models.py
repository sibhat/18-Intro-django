from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.
class Graph(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title= models.CharField(max_length=200)
    content=models.TextField(blank=True)
    tags = models.TextField(blank=True)
    author=models.TextField(
        max_length=100, default='no author'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add only set date at creatation
    last_modified = models.DateTimeField(auto_now=True)
    # autp_now set time at create and update

    def __repr__(self):
        return f"{title}"


class GraphWithUser(Graph): #inherits all field from Graph
    user = models.ForeignKey(User, on_delete=models.CASCADE)
