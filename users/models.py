from django.db import models

# Create your models here.
class Usuario(models.Model):
    gender_choice = (
        ('M', 'Man'),
        ('F', 'Female'),
    )

    code = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    first_name = models.CharField(null=False, max_length=100)
    last_name = models.CharField(null=True, max_length=100)
    email = models.EmailField(null=True, unique=True, max_length=100)
    profesion = models.CharField(max_length=100)
    genero = models.CharField(choices=gender_choice, max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"