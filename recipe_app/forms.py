from django import forms
from recipe_app.models import Author

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields= [
            'name',
            'bio'
        ]

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=150)
    instructions = forms.CharField(widget=forms.Textarea)

class AddRecipeAdminForm(forms.Form):
    title = forms.CharField(max_length=150)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=150)
    instructions = forms.CharField(widget=forms.Textarea)

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100)
    bio = forms.CharField(max_length=150)
    username = forms.CharField(max_length=36)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=36)
    password = forms.CharField(widget=forms.PasswordInput)
