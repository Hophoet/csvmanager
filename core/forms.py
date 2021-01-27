from django import forms
from .models import Csv


class CsvModalForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file1', 'file2', 'actions')
