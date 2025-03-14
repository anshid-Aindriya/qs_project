from django.db import models

from django import forms

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=255)
    question = models.TextField()  # Ensure 'question' matches in forms and templates

    def __str__(self):
        return self.name

class Email(models.Model):  # Renamed `email` to `Email`
    email = models.EmailField(unique=True)  # Add `unique=True` to prevent duplicates

    def __str__(self):
        return self.email