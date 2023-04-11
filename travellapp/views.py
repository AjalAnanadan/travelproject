from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import meet
# Create your views here.
def demo(request):
    obj=place.objects.all(),
    people=meet.objects.all()
    return  render(request,"index.html",{'objs':obj,'pep':people})
#def addition(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # result1=x+y
    #result2=x-y
   # result3=x*y
    #result4=x%y
    #return  render(request,"result.html",{'res':result1,'res1':result2,'res2':result3,'res3':result4})


