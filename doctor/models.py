from django.db import models

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)  # Hash before storing
    qualification = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    license = models.CharField(max_length=50)
    certificate = models.FileField(upload_to='certificates/')
    idproof = models.FileField(upload_to='idproofs/')
    fingerprint_data = models.TextField(blank=True, null=True)

    def __str__(self):
         return f"{self.first_name}-{self.last_name}-{self.gender}-{self.address}-{self.phone}-{self.email}-{self.username}-{self.password}-{self.qualification}-{self.specialization}-{self.experience}-{self.license}-{self.certificate}-{self.idproof}"
    
    
