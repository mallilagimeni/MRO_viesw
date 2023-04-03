from django.db import models

# Create your models here.
class Topic(models.Model):
    topics_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topics_name

class WebPages(models.Model):
    topics_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()
    def __str__(self):
        return self.name
        


class AcessRecords(models.Model):
    name=models.ForeignKey(WebPages,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
    def __str__(self):
        return self.author