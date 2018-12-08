from django.db import models

# Create your models here.

class TimeStampleModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Image(TimeStampleModel):
    
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()

class Comment(TimeStampleModel):

    message = models.TextField()

