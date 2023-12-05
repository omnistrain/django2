from django.db import models
from django.contrib.auth.models import AbstractUser, Group


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.CREATOR:
            group = Group.objects.get(name='creators')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)
