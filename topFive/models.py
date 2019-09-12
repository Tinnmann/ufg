from django.db import models

class TopFive(models.Model):
    seriesTitle = models.CharField(max_length=100)
    novelTitle = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    seriesSummary = models.TextField()
    novelSummary = models.TextField()
    image = models.FilePathField(path="/img")
