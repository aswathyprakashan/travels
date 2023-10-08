from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import person


# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=person.objects.all()
    return render(request, "index.html",{'result': obj,'per': obj1})




# def about(request):
#     return HttpResponse("ABOUT")
#
# def contact(request):
#     return render(request,"contact.html")
#
# def detail(request):
#     return HttpResponse("DETAILS")

# def operations(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     sub=x-y
#     mul=x*y

