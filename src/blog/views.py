from django.forms import formset_factory, modelformset_factory
from django.utils import timezone
from django.shortcuts import render

from .models import Post
from .forms import TestForm, PostModelForm

# Create your views here.

def formset_view(request):
	PostModelFormset = modelformset_factory(Post, fields=['user', 'title', 'slug'])
	formset = PostModelFormset(request.POST or None, queryset=Post.objects.filter(id__gt=4))

	if formset.is_valid():
		for form in formset:
			print(form.cleaned_data)
			obj = form.save(commit=False)
			if form.cleaned_data:
				obj.title = "This title"
				obj.publish = timezone.now()
				obj.save()

	template = "formset_view.html"
	context = {
		"formset": formset
	}
	return render(request, template, context)


# def formset_view(request):
# 	TestFormset = formset_factory(TestForm, extra=2)
# 	formset = TestFormset(request.POST or None)

# 	if formset.is_valid():
# 		for form in formset:
# 			print(form.cleaned_data)

# 	template = "formset_view.html"
# 	context = {
# 		"formset": formset
# 	}
# 	return render(request, template, context)

def home(request):
	form = PostModelForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.title = "Some random title"
		obj.publish = timezone.now()
		obj.save()
	if form.has_error:
		# print("15", form.errors)
		# print("16", form.errors.as_json())
		# print("17", form.errors.as_text())
		data = form.errors.items()
		for key, value in data:
			# print(key, value)
			# print(dir(value))
			# print(dir(key))
			error_str = "{field}: {error}".format(field=key, error=value.as_text())
			print(error_str)

		# print(form.non_field_errors())


	# initial_dict = {
	# 	# "some_text": "Text",
	# 	"boolean": True,
	# 	"integer": 123,
	# }
	# form = TestForm(request.POST or None, initial=initial_dict)
	# if form.is_valid():
	# 	print(form.cleaned_data)


	# form = TestForm()
	# if request.method == "POST":
	# 	form = TestForm(data=request.POST)
	# 	print(request.POST)
	# 	print(request.POST.get("search"))
	# elif request.method == "GET":
	# 	print(request.GET)
	# 	form = TestForm(user=request.user)

	template = "form.html"
	context = {
		"form": form
	}
	return render(request, template, context)