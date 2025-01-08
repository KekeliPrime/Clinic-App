from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    full_name = models.CharField(max_length=60, null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=False, null=True)
    student_id = models.CharField(max_length=10, null=True, blank=False, unique=True)
    address = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=False, null=True, unique=True)
    is_nurse = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    is_lecture = models.BooleanField(default=False)
    is_sammykeys = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'student_id']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class AppointmentSlot(models.Model):
    nurse = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_nurse': True})
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nurse.full_name} - {self.start_time} to {self.end_time}"


class BookAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, limit_choices_to={'is_student': True})
    appointment_slot = models.ForeignKey(AppointmentSlot, on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.appointment_slot.is_occupied:
            raise ValueError("This appointment slot is already occupied.")
        else:
            self.appointment_slot.is_occupied = True
            self.appointment_slot.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.full_name} - {self.appointment_slot}"
