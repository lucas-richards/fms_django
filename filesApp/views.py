from django.shortcuts import render
from .models import File
# Create your views here.

  

def files_index(request):
    files = File.objects.filter()
    return render(request, 'filesApp/files_index.html', {
        'files': files,
    })

def file_detail(request, name):
    file = File.objects.get(doc=name)
    return render(request, 'filesApp/file_detail.html', {
        'file': file,
    })