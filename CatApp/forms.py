from django.forms import ModelForm
from .models import CatPicture

class CatForm(ModelForm):
    class Meta:
        model = CatPicture
        fields = ['breed', 'cat_name', 'photo']
