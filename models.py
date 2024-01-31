from django.db import models


class allaboutme (models.Model):
    FirstName = models.TextField(max_length=200, blank=True)
    Lastname = models.TextField(max_length=200, blank=True)
    phone =models.TextField(max_length=20, blank=True)
    email = models.TextField(max_length=30, blank=True)
    descript = models.TextField(max_length=800, blank=True)
    linkedin_URL = models.CharField(max_length=200, blank=True)
    Git_URL = models.TextField(max_length=200, blank=True)
    #picture = models.ImageField(upload_to='static/assets/img', blank=True)
    Company1 = models.TextField(max_length=200, blank=True)
    Experience1 =models.TextField(max_length=800, blank=True)
    Company2 = models.TextField(max_length=200, blank=True)
    Experience2 = models.TextField(max_length=800, blank=True)
    Company3 = models.TextField(max_length=200, blank=True)
    Experience3 = models.TextField(max_length=800, blank=True)
    Company4 = models.TextField(max_length=200, blank=True)
    Experience4 = models.TextField(max_length=800, blank=True)
    Diplome1 = models.TextField(max_length=100, blank=True)
    Description1 = models.TextField(max_length=100, blank=True)




