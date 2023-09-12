from django.db import models
from django.urls import reverse
# Create your models here.
class Beer(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    flavour = models.CharField(max_length=150)
    food_mate = models.CharField(max_length=150)
    country = models.CharField(max_length=50)
#After creating models.py we have to update this table in database by using py manage.py makemigrations from cmd and after we have to migrate it by typing py manage.py migrate, after migration successfully, we will create superuser by typing py manage.py createsuperuser from cmd.
    def get_absolute_url(self):
        return reverse('list')
