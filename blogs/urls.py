from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
    path('blogslist/', views.Blog_list),
    path('contacts/', views.create_contact),
     path('registeredemails/', views.registered_emails),
] 