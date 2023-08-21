from django.db import models

# Create your models here.
class Measurement(models.Model):
    feet = models.PositiveIntegerField(default=0)
    inches = models.PositiveIntegerField(default=0)
    numerator = models.PositiveIntegerField(default=0)
    denominator = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.feet} and {self.inches} and {self.numeratorInches}/{self.denominatorInches}'