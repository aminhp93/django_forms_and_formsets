from django.shortcuts import render

from .forms import TestForm

# Create your views here.
def home(request):
	form = TestForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)


	# form = TestForm()
	# if request.method == "POST":
	# 	print(request.POST)
	# 	print(request.POST.get("search"))
	# elif request.method == "GET":
	# 	print(request.GET)

	template = "form.html"
	context = {
		"form": form
	}
	return render(request, template, context)