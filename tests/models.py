from pgsphere.fields import SBoxField
from django.db import models


class SBox(models.Model):
    area = SBoxField()

    def __str__(self):
        return self.area
