from django.shortcuts import render

from .forms import TestForm

# Create your views here.
def home(request):
	# initial_dict = {
	# 	# "some_text": "Text",
	# 	"boolean": True,
	# 	"integer": 123,
	# }
	# form = TestForm(request.POST or None, initial=initial_dict)
	# if form.is_valid():
	# 	print(form.cleaned_data)


	form = TestForm()
	if request.method == "POST":
		form = TestForm(data=request.POST)
		print(request.POST)
		print(request.POST.get("search"))
	elif request.method == "GET":
		print(request.GET)
		form = TestForm(user=request.user)

	template = "form.html"
	context = {
		"form": form
	}
	return render(request, template, context)