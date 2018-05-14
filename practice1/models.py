from django.db import models


# Create your models here.
# ( ) => 繼承
class Post(models.Model):
    # CharField 單行文字 unique 不重複
    title = models.CharField(max_length=255, unique= True)
    # TextField 多行文字
    content = models.TextField(max_length=255)

    def __str__(self):
        return self.title