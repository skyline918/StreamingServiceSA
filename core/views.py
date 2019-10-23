from django.shortcuts import render

# Create your views here.
from .models import Video


def home(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, template_name='home.html', context=context)
