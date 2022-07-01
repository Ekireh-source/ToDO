from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    item = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('authentication.User', related_name='todo', on_delete=models.CASCADE)



    def __str__(self):
        return self.title

