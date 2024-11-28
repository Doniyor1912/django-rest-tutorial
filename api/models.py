from django.db import models
class Container(models.Model):
    name = models.CharField(max_length=20)
    context = models.TextField()
    is_done = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name