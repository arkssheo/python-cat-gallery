from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import CatPicture
from .forms import CatForm

# Create your views here.
def index(request):
    return render(request, 'CatApp/index.html')

def new_cat(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            request.session['new_cat'] = form.cleaned_data['cat_name']
            new_cat = CatPicture(cat_name=form.cleaned_data['cat_name'])
            new_cat.save()
            return HttpResponseRedirect('/gallery/')
    else:
        form = CatForm()
    return render(request, 'CatApp/newcat.html', { 'form': form })

def delete_cat(request, cat_id):
    try:
        cat = CatPicture.objects.get(pk=cat_id)
    except CatPicture.DoesNotExist:
        raise Http404('Cat not found')
    cat.delete()
    return HttpResponseRedirect('/gallery/')

class ListView(generic.ListView):
    template_name = 'CatApp/list.html'
    context_object_name = 'cat_list'

    def get_queryset(self):
        return CatPicture.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #return context
        if 'new_cat' in self.request.session:
            context['new_cat'] = self.request.session.get('new_cat', 'unknown')
            del self.request.session['new_cat']
        return context
