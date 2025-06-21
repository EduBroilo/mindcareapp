from django.db import models

# Create your models here.
class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    therapist_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.patient_name} with {self.therapist_name} on {self.date} at {self.time}"