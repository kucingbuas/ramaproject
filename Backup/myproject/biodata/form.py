from django.forms import ModelForm 
from .models import Biodata

class CustomerForm(ModelForm):
    class Meta:
        model = Biodata
        fields = '__all__'