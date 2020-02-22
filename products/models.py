from django.db import models

class Attr(models.Model):
    article = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    name_model = models.CharField(max_length=20, null=True, blank=True)
    name_kor = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=50)
    price_sale = models.IntegerField(default=0)
    price_order = models.IntegerField(default=0)
    delivery_price = models.IntegerField(default=0)
    delivery_send = models.CharField(max_length=100)
    delivery_return = models.CharField(max_length=100)
    company_make = models.CharField(max_length=20)
    company_sale = models.CharField(max_length=20)
    company_as = models.CharField(max_length=20)
    inform = models.TextField()

    def __str__(self):
        return self.article

class Cont(models.Model):
    group = models.CharField(max_length=20)
    contents = models.TextField()

    def __str__(self):
        return self.group
