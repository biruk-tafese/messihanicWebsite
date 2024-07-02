from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import BlogSerializers
from .serializers import ContactSerializer
from .serializers import RegisteredEmailsSerializer
from .models import RegisteredEmails
from django.http import JsonResponse


@api_view(['GET'])

def Blog_list(request):
    posts = Post.objects.all()
    serializer = BlogSerializers(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_contact(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['POST'])
def registered_emails_view(request):
    if request.method == 'POST':
        # Handle the POST request logic here
        email = request.data.get('email')  # Retrieve the email from the request

        # Create a new RegisteredEmails object and save it to the database
        registered_email = RegisteredEmails(email=email)
        registered_email.save()

        return JsonResponse({'message': 'Email registered successfully'})  # Return a JSON response
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)  # Return an error response for other methods


@api_view(['GET'])
def registered_emails(request):
    emails = RegisteredEmails.objects.all()
    serializer = RegisteredEmailsSerializer(emails, many=True)
    return Response(serializer.data)


