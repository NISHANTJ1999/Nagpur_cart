from django.shortcuts import render

# Create your views here.
def store(request):
    context = {}
    
    return render(request,'Ecart/store.html', context)

def cart(request):
    context = {}
    
    return render(request,'Ecart/cart.html', context)


def checkout(request):
    context = {}
    
    return render(request,'Ecart/checkout.html', context)

