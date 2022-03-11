
from django.db import models


class Requests(models.Model):

    name = models.CharField('Аты-жөні', max_length=100)
    phone_number = models.CharField('Номер', max_length=100)
    hotel = models.CharField('Қонақ үй', max_length=100)
    child = models.IntegerField('Балалар саны')
    adult = models.IntegerField('Балалар саны')
    date1 = models.DateField('Алу куны')
    date2 = models.DateField('Откізу күні')









