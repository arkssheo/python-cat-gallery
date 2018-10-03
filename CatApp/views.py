from django.shortcuts import render
from django.views import generic
from .models import CatPicture

# Create your views here.
def index(request):
    return render(request, 'CatApp/index.html')

class ListView(generic.ListView):
    template_name = 'CatApp/list.html'
    context_object_name = 'cat_list'

    def get_queryset(self):
        return CatPicture.objects.all()
