# Hospital/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    reason = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, default='0000000000')
    admission = models.DateField()
    discharge = models.DateField()
    docname = models.ForeignKey('Doctor', on_delete=models.CASCADE)  # Avoids circular import

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)  # String reference
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)  # String reference
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return f'Appointment for {self.patient} with {self.doctor}'

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
