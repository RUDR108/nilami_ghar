from django.shortcuts import render
from homePage.models import Item
from store.models import Product
from django.db.models import Q
from accounts.forms import RegistrationForm

def home(request):
    products=Product.objects.all().filter(is_available=True)

    context={
        'products':products,
    }
    return render(request,"home.html",context)

# def update(request):
#     if request.method=='GET':
#         form=RegistrationForm()
#         if form.is_valid():
#             bid_added= form.cleaned_data['bid_added']
#             messages.success(request,'Registration successful')
#             if bid_added>Product.price:
#                 Product.price=bid_added
#             product.save()
#     return render(request,'home.html')

# def search(request):
#     context={}
#     if request.method=='GET': 
#         keyword=request.GET.get('Keyword',False)
#         print(keyword)
#         if keyword:
#             products=Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword)|Q(product_name__icontains=keyword))
#             product_count = products.count()
#             context={
#                 'products':products,
#                 'product_count':product_count,
#              }
#     return render(request,'home.html',context)