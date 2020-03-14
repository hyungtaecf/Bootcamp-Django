from django import forms
from forms_app.models import Suggestion
from django.core import validators

class Suggestions(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget = forms.Textarea, label="Suggestion:")

class SuggestionForm(forms.ModelForm):
    name = forms.CharField(validators= [validators.MinLengthValidator(4)])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    message = forms.CharField(widget = forms.Textarea, label="Suggestion:")

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

    class Meta:
        model = Suggestion
        exclude = ['verify_email']
