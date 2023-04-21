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
    CURRENCY = (('Dollar USA', 'USD'), ('Рубль', 'RUB'), ('EURO', 'EURO'), ('Тенге', 'Tenge'))
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, related_name='currencies')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, )
    valuta = models.CharField(choices=CURRENCY)
    buy = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    sell = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.valuta}, {self.created_at},{self.organisation}'


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='ragtins', verbose_name='Владелец рейтинга')
    org = models.ForeignKey(Organisations, on_delete=models.CASCADE, related_name='ratings', verbose_name='Организация')
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.org}, {self.rating}'

class Comment(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Владелец коммента')
    org = models.ForeignKey(Organisations,on_delete=models.CASCADE, related_name='comments', verbose_name='Организация')
    comment = models.TextField()

    def __str__(self):
        return f'{self.owner},{self.org}.{self.comment}'

