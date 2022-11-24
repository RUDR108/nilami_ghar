from django.shortcuts import render,get_object_or_404
from .models import Product
from accounts.models import Account
# from category.models import Category
# from carts.views import _cart_id,CartItem
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q

# Create your views here.

def store(request,category_slug=None):    #store 
    categories=None 
    products=None
    paged_products=None

    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories,is_available=True)
        paginator = Paginator(products,6)
        page =request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products=Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products,3)
        page =request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context={
        'products':paged_products,
        'product_count':product_count
    }
    return render(request,'store/store.html',context)


def product_detail(request,product_slug):  #detail for each product 
    try:
        single_product = Product.objects.get(slug=product_slug)
       
    except Exception as e:
        raise e
    if 'bid_added' in request.GET:
        keyword=request.GET['bid_added']
        
        if keyword:
            if(single_product.price<int(keyword)):
                single_product.price=keyword
                print(Account.first_name)
                single_product.current_winner=request.user.username
                single_product.save()
    context = {
        'single_product':single_product,
    }
    return render(request,'store/product_detail.html',context)

def search(request):
    context={}

    if 'keyword' in request.GET:
        print("something")
        keyword=request.GET['keyword']
        if keyword:
            products=Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword)|Q(product_name__icontains=keyword))
            product_count = products.count()
        context={
            'products':products,
            'product_count':product_count,
            }
    return render(request,'home.html',context)