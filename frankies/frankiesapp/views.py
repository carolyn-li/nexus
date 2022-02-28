from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def hello_world(request):
    return render(request, 'frankiesapp/hello_world.html')

def add_product(request):
    if(request.method=="POST"):
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_image = request.POST.get('product_imagee')
        product_materialsused = request.POST.get('product_materialsused')
        product_quantity = request.POST.get('product_quantity')
        product_unitprice = request.POST.get('product_unitprice')
        product_type = request.POST.get('product_type')
        product_visibility = request.POST.get('product_visibility')
        product_colors = request.POST.get('product_colors')
        if product_visibility == 'on':
            product_visibility == True
        else:
            product_visibility == False
        try:
            Product.objects.create(product_name=product_name, 
            product_description=product_description, 
            product_image=product_image,  
            product_materialsused= product_materialsused,  
            product_quantity= product_quantity, 
            product_unitprice=product_unitprice, 
            product_type=product_type, 
            product_visibility=product_visibility, 
            product_colors=product_colors)

            message = "Product created successfully"
            return redirect(f'/Product?message={message}')
    
        except Exception as e:
            message = e
            context = {'message':message}
            return render(request, 'frankiesapp/add_product.html', context)

    else:
        return render(request, 'frankiesapp/add_product.html')

    return render(request, 'frankiesapp/add_product.html')