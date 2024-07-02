from rest_framework import serializers
from .models import Post
from .models import Contact
from .models import RegisteredEmails


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'date']  # Include 'image' here


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']

class RegisteredEmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredEmails
        fields = ['email']  # Add more fields as needed