from django.shortcuts import render
from .models import Student

# Create your views here.
def create(request):

    return render(request, 'students/create.html')
