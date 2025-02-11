from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    pub_data = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.CharField(max_length=32)

    def __str__(self):
        return self.title