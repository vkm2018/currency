from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Organisations(models.Model):
    TYPE = (('Bank', 'Bank'), ('Buro', 'Buro'))
    type = models.TextField(choices=TYPE, default='Buro')
    title = models.CharField(max_length=100)
    adress = models.TextField()
    number_phone = models.BigIntegerField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='buro')

    def __str__(self):
        return self.title

class Currency(models.Model):
    CURRENCY = (('Dollar USA', 'USD'), (''))
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, related_name='currencies')

    buy = models.IntegerField(default=0)
    sell = models.IntegerField(default=0)

