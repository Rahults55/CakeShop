from django.http import HttpResponse
from django.shortcuts import render
from .models import cake_intro, about, items, orange, blueberry, banana, apple, mango, strawberry, customer_say


# Create your views here.
def fun(request):
    obj = cake_intro.objects.all()
    obj1 = about.objects.all()
    obj2 = items.objects.all()
    obj3 = orange.objects.all()
    obj4 = blueberry.objects.all()
    obj5 = banana.objects.all()
    obj6 = apple.objects.all()
    obj7 = mango.objects.all()
    obj8 = strawberry.objects.all()
    obj9 = customer_say.objects.all()
    return render(request,"index.html",{'results': obj,'resul':obj1,'itms':obj2,'orngs':obj3,'blueb':obj4,'bana':obj5,'app':obj6,'mang':obj7,'strawb':obj8,'cust':obj9})

def org_details(request,orange_id):
    obj3 = orange.objects.all()
    return render(request,"orange_details.html",{'orngs':obj3})