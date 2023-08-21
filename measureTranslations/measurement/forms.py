from django import forms
from .models import Measurement

class MeasurementTranslateForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['feet', 'inches',
                   'numerator', 'denominator']