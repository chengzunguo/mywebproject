from django.shortcuts import render

from myapp.models import myModel
# Create your views here.

def home(request):
    mymodel = myModel.objects
    return render(request, 'home.html', {'info': 'Welcome to chengzunguo.com !','modeltext':mymodel})