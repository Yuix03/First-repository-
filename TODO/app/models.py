from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    STATUS=(
        ['Endbajarilad','Endbajarilad'],
        ['Bajarilyabt','Bajarilyabt']

    )
    title=models.CharField(max_length=50)
    time=models.TimeField(null=True)
    status=models.CharField(choices=STATUS,max_length=50)
    description=models.TextField(null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title