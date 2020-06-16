from django.db import models


# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=40)
    Email_id = models.EmailField()
    Subject = models.CharField(max_length=150)
    Message = models.TextField()

    def __str__(self):
        return self.Name


class Pdf(models.Model):
    image = models.ImageField(upload_to='images')
    pdf_body = models.FileField(upload_to='Pdf Files')
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def img(self):
        return self.image


class Register(models.Model):
    Username = models.CharField(max_length=40)
    Name = models.CharField(max_length=40)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Username
