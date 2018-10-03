from django.contrib import admin
from .models import CatPicture

# Register your models here.
class CatPictureAdmin(admin.ModelAdmin):
    fields = ['cat_name', 'breed']

admin.site.register(CatPicture, CatPictureAdmin)
