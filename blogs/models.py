from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = RichTextField()
    date = models.DateField()
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    # Add more fields as needed

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    message = models.TextField()
    # Add more fields as needed

class RegisteredEmails(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.email, self.subscribed_at}
