from django.shortcuts import render

from .forms import SearchForm

# Create your views here.
def home(request):
	form = SearchForm()
	template = "form.html"
	context = {
		"form": form
	}
	return render(request, template, context)