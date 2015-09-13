from django.db import models

class CustomDateField(models.DateField):
    def from_db_value(self, value, expression, connection, context):
        return value.__str__()

class Doctor(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Application(models.Model):
    CHOICES_TIME = (
        (1, "09:00"),
        (2, "10:00"),
        (4, "11:00"),
        (8, "12:00"),
        (16, "13:00"),
        (32, "14:00"),
        (64, "15:00"),
        (128, "16:00"),
        (256, "17:00"),
    )
    doctor =  models.ForeignKey(Doctor, blank=False, null=False)
    applicant = models.CharField(max_length=30)
    date = CustomDateField()
    time = models.SmallIntegerField(choices=CHOICES_TIME)
