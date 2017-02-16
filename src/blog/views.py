from django.utils import timezone
from django.shortcuts import render

from .forms import TestForm, PostModelForm

# Create your views here.
def home(request):
	form = PostModelForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.title = "Some random title"
		obj.publish = timezone.now()
		obj.save()


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