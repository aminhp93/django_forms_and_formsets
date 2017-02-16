from django import forms

from .models import Post

class PostModelForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ["user", "title", "slug"]
		# exclude = ["title"]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		print(title)
		return title

	def save(self, commit=True, *args, **kwargs):
		obj = super().save(commit=False, *args, **kwargs)
		obj.publish = "2017-05-29"
		obj.title = "New title"
		obj.content = "Comming soon"
		
		if commit:
			obj.save()
		return obj

SOME_CHOICES = (
		('value_1', 'VALUE_1'),
		('value_2', 'VALUE_2'),
		('value_3', 'VALUE_3'),
	)

INTS_CHOICES = [tuple([x, x]) for x in range(0, 100)]

YEARS = [x for x in range(1980, 2020)]

class TestForm(forms.Form):
	date_field = forms.DateField(initial="2017-01-02", widget=forms.SelectDateWidget(years=YEARS))
	some_text = forms.CharField(label="Text", widget=forms.Textarea(attrs={"rows": 4, "cols": 10}))
	choices = forms.CharField(label="Choice", widget=forms.RadioSelect(choices=SOME_CHOICES))
	boolean = forms.BooleanField()
	integer = forms.IntegerField(initial=10, widget=forms.Select(choices=INTS_CHOICES))
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
	