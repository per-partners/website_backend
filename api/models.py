from django.db import models
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    body = models.TextField(default=" ")
    image = models.ImageField(null=True)
    tags = models.JSONField(null=True)

    def __str__(self):
        return str(self.title)


class Careers(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return str(self.title)


class CVS(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Assumes you have a 'pdfs' directory in your MEDIA_ROOT
    pdf = models.FileField(upload_to='pdfs/')
    email = models.EmailField(max_length=100)
    seniority = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MyCVS(APIView):
    # Enable file upload support
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        # Extract and validate the data from the request
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        # Assuming this is a file field in your form
        pdf = request.data.get('pdf')
        email = request.data.get('email')
        seniority = request.data.get('seniority')

        # Validate and process the data as needed
        if not all([first_name, last_name, pdf, email, seniority]):
            return Response({'message': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the data to your model
        my_model = CVS(
            first_name=first_name,
            last_name=last_name,
            pdf=pdf,
            email=email,
            seniority=seniority
        )
        my_model.save()

        return Response({'message': 'Data saved successfully'}, status=status.HTTP_201_CREATED)
