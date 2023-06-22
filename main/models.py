from django.db import models

class House(models.Model):
    floors = models.IntegerField()
    apartments = models.IntegerField()
    address = models.CharField(max_length=255)
    year_built = models.IntegerField()

    def __str__(self):
        return self.address


class Tenant(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=80)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Payment(models.Model):
    STATUS_CHOICES = [
        ('payed', 'Оплачен'),
        ('not_payed', 'Не оплачен'),
    ]
    date = models.DateField()
    sum = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='not_payed',
    )
    address = models.ForeignKey(House, on_delete=models.CASCADE, null=True, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

