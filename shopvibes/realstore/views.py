
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import CustomerRegisterationForm, LoginForm
from django.contrib import messages

from .models import Product 
# Create your views here.
# def home(request):
#     return render(request, 'realstore/home.html')

class ProductView(View):
    def get(self, request):
        topwears=Product.objects.filter(category='TW')
        bottomwears=Product.objects.filter(category='BW')
        mobiles=Product.objects.filter(category='M')
        return render(request, 'realstore/home.html', {'topwears':topwears , 'bottomwears': bottomwears, 'mobiles': mobiles})

def mobile(request, data=None):
    if data==None:
        mobiles=Product.objects.filter(category='M')
    elif (data=='mi' or data=='samsung' or data=='redmi' or data=='apple'):
        mobiles=Product.objects.filter(category='M').filter(brand=data)
    elif (data=='below'):
        mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=30000)
    elif (data=='above'):
        mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=30000)

    return render(request, 'realstore/mobile.html', {'mobiles':mobiles})

def profile(request):
    return render(request, 'realstore/profile.html')

# def customerregistration(request):
#     return render(request, 'realstore/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form=CustomerRegisterationForm()
        return render(request, 'realstore/customerregistration.html', {'form': form})
    def post(self, request):
        form=CustomerRegisterationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registered Succesfully')
            form.save()
        return render(request, 'realstore/customerregistration.html', {'form': form})


# def login(request):
#     return render(request, 'realstore/login.html')

# class LoginView(View):
#     def get(self, request):
#         form=LoginForm()
#         return render(request, 'realstore/login.html', {'form': form})
        

def addToCart(request):
    return render(request, 'realstore/addtocart.html')


def orders(request):
    return render(request, 'realstore/orders.html')

# def productDetail(request):
#     return render(request, 'realstore/productdetail.html')
class productDetailView(View):
    def get(self, request, pk):
        unique_product=Product.objects.get(pk=pk)
        return render(request, 'realstore/productdetail.html', {'unique_product':unique_product})


def address(request):
    return render(request, 'realstore/address.html')

def checkout(request):
    return render(request, 'realstore/checkout.html')

def buyNow(request):
    return render(request, 'realstore/buynow.html')
