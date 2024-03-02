from django.db import models


class Country(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):

    name = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Location(models.Model):

    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None)

    # Необходимо, чтобы после выбора страны были доступны только ее регионы
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=None)
    # Также и с городами
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.city.name)
