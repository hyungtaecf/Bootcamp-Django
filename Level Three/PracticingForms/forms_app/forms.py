from django import forms

class Suggestions(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget = forms.Textarea)
