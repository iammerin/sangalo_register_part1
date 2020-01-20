from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=15)

    def __str__(self):
        return self.country_name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name


# class Post(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     post_code = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.post_code


class Suburb(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=25)
    suburb_name = models.CharField(max_length=35)

    def __str__(self):
        return self.suburb_name
