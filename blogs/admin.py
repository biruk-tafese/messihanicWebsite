from django.contrib import admin
from .models import Post, Contact, RegisteredEmails

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(RegisteredEmails)

