from django.db import models

class Rv(models.Model):
    name = models.CharField(max_length=300)
    manufacturer = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} {self.manufacturer}"

    def get_absolute_url(self):
        return f"/rv/{self.pk}" 

class Renter(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return f"/renter/{self.pk}" 

class Rent(models.Model):
    renter = models.ForeignKey('Renter', on_delete=models.CASCADE)
    rv = models.ForeignKey('Rv', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.renter} {self.rv}"

    def get_absolute_url(self):
        return f"/rent/{self.pk}" 
