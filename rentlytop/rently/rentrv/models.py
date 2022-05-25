from django.db import models

class Rv(models.Model):
    name = models.CharField(max_length=300)
    manufacturer = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} {self.manufacturer}"

    def get_absolute_url(self):
        return f"/rv/{self.pk}" 
