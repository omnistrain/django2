from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE = {
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné')
    }

    photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE)