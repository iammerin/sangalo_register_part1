from django.db import models


class Country1(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=15)

    def __str__(self):
        return self.country_name


class State1(models.Model):
    country = models.ForeignKey(Country1, related_name='states', on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name


class Post1(models.Model):
    state = models.ForeignKey(State1, related_name='posts', on_delete=models.CASCADE)
    post_code = models.CharField(max_length=10)

    def __str__(self):
        return self.post_code


class Suburb1(models.Model):
    post = models.ForeignKey(Post1,related_name='suburbs', on_delete=models.CASCADE)
    # postal_code = models.CharField(max_length=25)
    suburb_name = models.CharField(max_length=35)

    def __str__(self):
        return self.suburb_name
