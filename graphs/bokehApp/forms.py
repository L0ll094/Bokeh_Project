from django import forms

class InputForm(forms.Form):
    scalar=forms.IntegerField(label="A number")
