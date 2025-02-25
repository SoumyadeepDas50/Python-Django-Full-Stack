from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Customer,Order,Tag
from .forms import OrderForm

# Create your views here.
def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()

    context={'orders':orders,'customers':customers,'total_orders':total_orders,'delivered':delivered,'pending':pending}

    return render(request,'accounts/dashboard.html',context)

def product(request):
    product=Product.objects.all()
    context={'product':product}
    return render(request,'accounts/product.html',context)

def customer(request, pk_test):
    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    order_count=orders.count()
    context={'customer':customer,'orders':orders,'order_count':order_count}
    return render(request,'accounts/customer.html',context)

def createorder(request):
    form=OrderForm()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={"form":form}
    return render(request,'accounts/order_form.html',context)

def updateorder(request,pk):
    order=Order.objects.get(id=pk) #it will return the particular product id
    form=OrderForm(instance=order) #this will show the product in form page
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'order':order,'form':form}
    return render(request, 'accounts/order_form.html',context)

def deleteorder(request,pk):
    order=Order.objects.get(id=pk) #it will return the particular product id
    if request.method=='POST':
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request, "accounts/delete.html",context)
    
            
