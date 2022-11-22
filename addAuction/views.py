from django.shortcuts import render
from store.models import Product
from .forms import AuctionForm
from django.contrib import messages,auth
from accounts.models import Account

# Create your views here.
# def addAuction(request):
#     context ={}
#     context['form']= AuctionForm()
#     return render(request, "addAuction.html", context)


def addAuction(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        
        if not form.is_valid():
            product_name = form.cleaned_data.get('product_name')
            

            description=form.cleaned_data.get('description')
            price = form.cleaned_data.get('price')
            images = request.FILES['images']
            Bid_owner=request.user.username
            product=Product.objects.create_product(product_name=product_name,description=description,price=price,images=images)
            product.stock=1
            product.slug =product_name
            # product.is_available = .BooleanField(default=True)
            # product.category=models.ForeignKey(Category,on_delete=models.CASCADE)
            # product.created_date=models.DateTimeField(auto_now_add=True)
            # product.modified_date=models.DateTimeField(auto_now_add=True)
            # user.phone_number=phone_number
            product.save()
            messages.success(request,'Product Updated')
            # return redirect('register')
        else:
            print("something")
    else:
        form=AuctionForm()

    context={
        'form':form,
    }
    
 
    
    return render(request,'addAuction.html',context)