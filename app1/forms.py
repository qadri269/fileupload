from .models import student
from django.forms import ModelForm
class myform(ModelForm):
    class Meta:
        model=student
        fields='__all__'