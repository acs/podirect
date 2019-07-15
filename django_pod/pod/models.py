from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)


class SKU(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class Retailer(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)


class PurchaseOrder(models.Model):
    buyer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    order = models.ManyToManyField(SKU)

