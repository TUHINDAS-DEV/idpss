# from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from story.models import *
def test(request):
    return HttpResponse('test my site')

def demo(request):
    return render(request,'demo.html')
def love(request):
    a=(request.GET['a1'])
    b=(request.GET['a2'])

    return HttpResponse(a+' '+'and'+' '+b+' '+'they are lovers')
def factorial(request):
    a=int(request.GET['f'])
    m=1
    for i in range(1,a+1):
        m=m*i
    return HttpResponse(m)
def demoo(request):
    return render(request,'demoo.html')



# Create your views here.
