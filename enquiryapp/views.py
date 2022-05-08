from django.shortcuts import render
from .forms import EnForm
from .models import EnModel

# Create your views here.

def home(request):
	if request.method =="POST":
		data = EnForm(request.POST)
		if data.is_valid():
			data.save()
			fm = EnForm()
			return render(request,"home.html",{"fm":fm , "msg":"We will get back to u"})
	else:
		fm = EnForm()
		return render(request,"home.html",{"fm":fm})
		
