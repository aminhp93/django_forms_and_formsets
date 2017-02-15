from django import forms

class TestForm(forms.Form):
	some_text = forms.CharField()
	boolean = forms.BooleanField()
	integer = forms.IntegerField(initial=10)
	email = forms.EmailField(min_length=10)

	def __init__(self, user=None, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if user:
			self.fields["some_text"].initial = user.username

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
	