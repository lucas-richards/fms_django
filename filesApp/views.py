from django.shortcuts import render
from .models import File
# Create your views here.

  

def files_index(request):
    files = File.objects.filter()
    return render(request, 'filesApp/files_index.html', {
        'files': files,
    })