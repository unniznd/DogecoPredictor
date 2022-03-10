from django import forms

class PredictorForm(forms.Form):
    close = forms.DecimalField()