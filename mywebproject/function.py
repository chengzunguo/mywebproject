'''
郭承尊
'''


from django.http import  HttpResponse
from django.shortcuts import  render


def home(request):
    # data = request.GET['text1']


    return render(request, 'home.html', {'info': 'Welcome to chengzunguo.com !'})


def count(request):
    line =request.GET['text1']
    print(type(line))
    print(line)
    return render(request, 'count.html', {'line':line})


