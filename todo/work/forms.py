from django.forms import ModelForm
from .models import Tlist

class Tform(ModelForm):
    class Meta:
        model = Tlist
        fields = ['title', 'status']