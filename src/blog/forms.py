from django import forms

class TestForm(forms.Form):
	some_text = forms.CharField()
	boolean = forms.BooleanField()
	integer = forms.IntegerField()
	email = forms.EmailField()

	def clean_integer(self, *args, **kargs):
		integer = self.cleaned_data.get("integer")
		if integer < 10:
			raise forms.ValidationError("The interger must be greater than 10")
		return integer

	def clean_some_text(self, *args, **kwargs):
		some_text = self.cleaned_data.get("some_text")
		if len(some_text) < 10:
			raise forms.ValidationError("At least 10 character")
		return some_text
	
