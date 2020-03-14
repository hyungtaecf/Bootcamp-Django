from django.shortcuts import render
from . import forms

# Create your views here.
def suggestions_view(request):
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            print("Form validation success! Prints in console.")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Suggestion: "+form.cleaned_data['message'])
            form.save(commit=True)
            return render(request,'forms_app/thanks.html')
    else:
        # form = forms.Suggestions()
        form = forms.SuggestionForm()
        return render(request,'forms_app/forms_page.html',{'suggestions_form':form})

def index(request):
    return render(request,'forms_app/index.html')

def thanks(request):
    return render(request,'forms_app/thanks.html')
