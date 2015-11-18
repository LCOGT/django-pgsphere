from pgsphere.fields import SBoxField, SPointField
from django.db import models


class SBox(models.Model):
    area = SBoxField()

    def __str__(self):
        return str(self.area)


class SPoint(models.Model):
    location = SPointField()

    def __str__(self):
        return str(self.location)
