from django import forms
class Employeeinfo(forms.Form):
    no = forms.IntegerField()
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username', 'required':'true'}))
    salary = forms.IntegerField()
    address = forms.CharField()
    