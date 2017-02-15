from django import forms

class TestForm(forms.Form):
	some_text = forms.CharField()
	boolean = forms.BooleanField()
	integer = forms.IntegerField()
	email = forms.EmailField()
	
