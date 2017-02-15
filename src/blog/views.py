from django.shortcuts import render

from .forms import TestForm

# Create your views here.
def home(request):
	form = TestForm()
	template = "form.html"
	context = {
		"form": form
	}
	return render(request, template, context)