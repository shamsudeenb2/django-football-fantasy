from django.db import models


# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    division = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Footballer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=120)
    date_of_birth = models.DateField()
    position = models.IntegerField(blank=True)
    jersy_number = models.IntegerField(blank=True)
    market_value = models.IntegerField(blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
