from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name")
    emergency_contact_name = models.CharField(blank=True, max_length=100)
    emergency_contact_phone_number = models.CharField(blank=True, max_length=9, validators=[MinLengthValidator(12)])
    media_permission = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ['name']

    def __str__(self):
        return self.name


class Signin(models.Model):
    is_signin = models.BooleanField(choices=[(True, "Sign in"), (False, "Sign out")], verbose_name="Sign in/out")
    date = models.DateTimeField(default=timezone.now)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sign in/out"

    def __str__(self):
        return f"{self.person} - {'Sign In' if self.is_signin else 'Sign Out'}"
