from django.db import models
from django.utils import timezone

# Create your models here.

class PictureInfoModel(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    class Meta:
        abstract = True

class CatPicture(PictureInfoModel):
    breed = models.CharField(max_length=80, blank=True, default='unknown')
    cat_name = models.CharField(max_length=120)
    def __str__(self):
        return self.cat_name
    def save(self, *args, **kwargs):
        """ on save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(CatPicture, self).save(*args, **kwargs)
