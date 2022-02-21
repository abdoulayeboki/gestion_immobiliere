from django.db import models
class Zone(models.Model):
    nomZone = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nomZone
