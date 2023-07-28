from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    completion = models.BooleanField(default=False)

    class Meta:
        ordering= ['completion','date']

    def __str__(self) -> str:
        return self.title